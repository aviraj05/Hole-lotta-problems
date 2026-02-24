from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
async def get_heatmap_data(city: str = "pune", min_severity: str = "minor"):
    """Returns GPS coordinates + severity weights for deck.gl heatmap rendering."""
    pass

@router.get("/hotspots")
async def get_hotspots(city: str = "pune", limit: int = 10):
    """Returns top N hotspot clusters ranked by report frequency and severity."""
    pass

@router.get("/road-health-index")
async def get_road_health_index(city: str = "pune"):
    """Returns zone-wise Road Health Index scores for the city."""
    pass
