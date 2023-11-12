"""Tests for raster functions."""
import gc
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import geopandas as gpd
import pandas as pd
import pytest
import rioxarray as rxr
import xarray as xr
from pytest import FixtureRequest

from gdptools import ZonalGen
from gdptools.data.user_data import UserTiffData


@pytest.fixture(scope="function")
def get_tiff_slope() -> xr.DataArray:
    """Get tiff slope file."""
    ds = rxr.open_rasterio("./tests/data/rasters/slope/slope.tif")  # type: ignore
    yield ds
    del ds
    gc.collect()


@pytest.fixture(scope="function")
def get_tiff_text() -> xr.DataArray:
    """Get tiff text_prms file."""
    ds = rxr.open_rasterio("./tests/data/rasters/TEXT_PRMS/TEXT_PRMS.tif")  # type: ignore
    yield ds
    del ds
    gc.collect()


@pytest.fixture(scope="function")
def get_gdf() -> gpd.GeoDataFrame:
    """Get gdf file."""
    gdf = gpd.read_file("./tests/data/Oahu.shp")
    yield gdf
    del gdf
    gc.collect()


@pytest.mark.parametrize(
    "vn,xn,yn,bd,bn,crs,cat,ds,gdf,fid",
    [
        (
            "slope",
            "x",
            "y",
            1,
            "band",
            26904,
            False,
            "get_tiff_slope",
            "get_gdf",
            "fid",
        ),
        (
            "TEXT_PRMS",
            "x",
            "y",
            1,
            "band",
            26904,
            True,
            "get_tiff_text",
            "get_gdf",
            "fid",
        ),
    ],
)
def test_cat_tiff_intersection(
    vn: str,
    xn: str,
    yn: str,
    bd: int,
    bn: str,
    crs: Any,
    cat: bool,
    ds: str,
    gdf: str,
    fid: str,
    request: FixtureRequest,
) -> None:
    """Test tiff intersection function."""
    data = UserTiffData(
        var=vn,
        ds=request.getfixturevalue(ds),
        proj_ds=crs,
        x_coord=xn,
        y_coord=yn,
        bname=bn,
        band=bd,
        f_feature=request.getfixturevalue(gdf),
        id_feature=fid,
        proj_feature=crs,
    )
    tmpdir = TemporaryDirectory()
    zonal_gen = ZonalGen(
        user_data=data,
        zonal_engine="serial",
        zonal_writer="csv",
        out_path=tmpdir.name,
        file_prefix="tmpzonal",
    )
    stats = zonal_gen.calculate_zonal(categorical=cat)

    assert isinstance(stats, pd.DataFrame)
    file = Path(tmpdir.name) / "tmpzonal.csv"
    assert file.exists()


@pytest.mark.parametrize(
    "vn,xn,yn,bd,bn,crs,cat,ds,gdf,fid",
    [
        (
            "slope",
            "x",
            "y",
            1,
            "band",
            26904,
            False,
            "get_tiff_slope",
            "get_gdf",
            "fid",
        ),
        (
            "TEXT_PRMS",
            "x",
            "y",
            1,
            "band",
            26904,
            True,
            "get_tiff_text",
            "get_gdf",
            "fid",
        ),
    ],
)
def test_cat_tiff_intersectio_p(
    vn: str,
    xn: str,
    yn: str,
    bd: int,
    bn: str,
    crs: Any,
    cat: bool,
    ds: str,
    gdf: str,
    fid: str,
    request: FixtureRequest,
) -> None:
    """Test tiff intersection function."""
    data = UserTiffData(
        var=vn,
        ds=request.getfixturevalue(ds),
        proj_ds=crs,
        x_coord=xn,
        y_coord=yn,
        bname=bn,
        band=bd,
        f_feature=request.getfixturevalue(gdf),
        id_feature=fid,
        proj_feature=crs,
    )
    tmpdir = TemporaryDirectory()
    zonal_gen = ZonalGen(
        user_data=data,
        zonal_engine="parallel",
        zonal_writer="csv",
        out_path=tmpdir.name,
        file_prefix="tmpzonal",
    )
    stats = zonal_gen.calculate_zonal(categorical=cat)

    assert isinstance(stats, pd.DataFrame)
    file = Path(tmpdir.name) / "tmpzonal.csv"
    assert file.exists()


@pytest.mark.parametrize(
    "vn,xn,yn,bd,bn,crs,cat,ds,gdf,fid",
    [
        (
            "slope",
            "x",
            "y",
            1,
            "band",
            26904,
            False,
            "get_tiff_slope",
            "get_gdf",
            "fid",
        ),
        (
            "TEXT_PRMS",
            "x",
            "y",
            1,
            "band",
            26904,
            True,
            "get_tiff_text",
            "get_gdf",
            "fid",
        ),
    ],
)
def test_cat_tiff_intersectio_d(
    vn: str,
    xn: str,
    yn: str,
    bd: int,
    bn: str,
    crs: Any,
    cat: bool,
    ds: str,
    gdf: str,
    fid: str,
    request: FixtureRequest,
) -> None:
    """Test tiff intersection function."""
    from dask.distributed import Client, LocalCluster

    cluster = LocalCluster(threads_per_worker=os.cpu_count())
    client = Client(cluster)  # type: ignore
    data = UserTiffData(
        var=vn,
        ds=request.getfixturevalue(ds),
        proj_ds=crs,
        x_coord=xn,
        y_coord=yn,
        bname=bn,
        band=bd,
        f_feature=request.getfixturevalue(gdf),
        id_feature=fid,
        proj_feature=crs,
    )
    tmpdir = TemporaryDirectory()
    zonal_gen = ZonalGen(
        user_data=data,
        zonal_engine="dask",
        zonal_writer="csv",
        out_path=tmpdir.name,
        file_prefix="tmpzonal",
    )
    stats = zonal_gen.calculate_zonal(categorical=cat)
    client.close()  # type: ignore
    del client
    cluster.close()  # type: ignore
    del cluster

    assert isinstance(stats, pd.DataFrame)
    file = Path(tmpdir.name) / "tmpzonal.csv"
    assert file.exists()
