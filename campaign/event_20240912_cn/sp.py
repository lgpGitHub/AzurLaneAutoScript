from .campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger

MAP = CampaignMap('SP')
MAP.shape = 'K5'
MAP.camera_data = ['D3', 'F3']
MAP.camera_data_spawn_point = ['I2']
MAP.map_data = """
    ++ -- ME -- ++ -- ME -- ++ ++ ++
    -- -- -- ME ++ ME -- MS -- -- SP
    -- MB -- -- -- -- MS -- __ -- --
    -- -- -- ME ++ ME -- MS -- -- SP
    ++ -- ME -- ++ -- ME -- ++ ++ ++
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 8, 'siren': 3},
    {'battle': 1},
    {'battle': 2},
    {'battle': 3},
    {'battle': 4},
    {'battle': 5},
    {'battle': 6},
    {'battle': 7, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, K4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, K5, \
    = MAP.flatten()


class Config:
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['Fox']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_AMBUSH = False
    MAP_HAS_MYSTERY = False
    STAR_REQUIRE_1 = 0
    STAR_REQUIRE_2 = 0
    STAR_REQUIRE_3 = 0
    # ===== End of generated config =====

    MAP_CHAPTER_SWITCH_20241219 = True
    MAP_IS_ONE_TIME_STAGE = True
    STAGE_ENTRANCE = ['half', '20240725']
    INTERNAL_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (120, 255 - 49),
        'width': (1.5, 10),
        'prominence': 10,
        'distance': 35,
    }
    EDGE_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (255 - 49, 255),
        'prominence': 10,
        'distance': 50,
        'wlen': 1000
    }
    HOMO_CANNY_THRESHOLD = (75, 100)
    MAP_SWIPE_MULTIPLY = (1.194, 1.217)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (1.155, 1.176)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (1.121, 1.142)


class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=2):
            return True

        return self.battle_default()

    def battle_5(self):
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=0):
            return True

        return self.battle_default()

    def battle_7(self):
        return self.fleet_boss.clear_boss()
