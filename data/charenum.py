from enum import Enum
from typing import Optional, List


class KiMeter(Enum):
    KI_METER_2_GREEN = "KiMeter 2 Green"
    KI_METER_2_GREEN_10_RED_LR = "KiMeter 2 Green 10 Red LR"
    KI_METER_2_GREEN_4_ORANGE = "KiMeter 2 Green 4 Orange"
    KI_METER_2_GREEN_LR = "KiMeter 2 Green LR"
    KI_METER_3_GREEN = "KiMeter 3 Green"
    KI_METER_3_GREEN_4_ORANGE = "KiMeter 3 Green 4 Orange"
    KI_METER_3_GREEN_5_ORANGE = "KiMeter 3 Green 5 Orange"
    KI_METER_3_GREEN_LR = "KiMeter 3 Green LR"
    KI_METER_4_GREEN = "KiMeter 4 Green"
    KI_METER_4_GREEN_3_ORANGE = "KiMeter 4 Green 3 Orange"
    KI_METER_4_GREEN_4_ORANGE = "KiMeter 4 Green 4 Orange"
    KI_METER_4_GREEN_LR = "KiMeter 4 Green LR"


class Rarity(Enum):
    LR = "LR"
    UR = "UR"


class Class(Enum):
    EXTREME = "Extreme"
    SUPER = "Super"


class TypeEnum(Enum):
    AGL = "AGL"
    INT = "INT"
    PHY = "PHY"
    STR = "STR"
    TEQ = "TEQ"


class Transformation:
    transformed_name: str
    transformed_id: int
    transformed_class: Optional[Class]
    transformed_type: Optional[TypeEnum]
    transformed_super_attack: str
    transformed_eza_super_attack: Optional[str]
    transformed_ultra_super_attack: Optional[str]
    transformed_eza_ultra_super_attack: Optional[str]
    transformed_passive: str
    transformed_eza_passive: Optional[str]
    transformed_links: List[str]
    transformed_image_url: str
    transformed_active_skill: Optional[str]
    transformed_active_skill_condition: Optional[str]

    def __init__(self, transformed_name: str, transformed_id: int, transformed_class: Optional[Class], transformed_type: Optional[TypeEnum], transformed_super_attack: str, transformed_eza_super_attack: Optional[str], transformed_ultra_super_attack: Optional[str], transformed_eza_ultra_super_attack: Optional[str], transformed_passive: str, transformed_eza_passive: Optional[str], transformed_links: List[str], transformed_image_url: str, transformed_active_skill: Optional[str], transformed_active_skill_condition: Optional[str]) -> None:
        self.transformed_name = transformed_name
        self.transformed_id = transformed_id
        self.transformed_class = transformed_class
        self.transformed_type = transformed_type
        self.transformed_super_attack = transformed_super_attack
        self.transformed_eza_super_attack = transformed_eza_super_attack
        self.transformed_ultra_super_attack = transformed_ultra_super_attack
        self.transformed_eza_ultra_super_attack = transformed_eza_ultra_super_attack
        self.transformed_passive = transformed_passive
        self.transformed_eza_passive = transformed_eza_passive
        self.transformed_links = transformed_links
        self.transformed_image_url = transformed_image_url
        self.transformed_active_skill = transformed_active_skill
        self.transformed_active_skill_condition = transformed_active_skill_condition


class Welcome4Element:
    name: str
    title: str
    max_level: int
    max_sa_level: Optional[int]
    rarity: Rarity
    welcome4_class: Optional[Class]
    type: Optional[TypeEnum]
    cost: int
    id: int
    image_url: str
    leader_skill: str
    super_attack: str
    ultra_super_attack: Optional[str]
    passive: str
    links: List[str]
    categories: List[str]
    ki_meter: List[KiMeter]
    base_hp: int
    max_level_hp: int
    free_dupe_hp: Optional[int]
    rainbow_hp: Optional[int]
    base_attack: int
    max_level_attack: int
    free_dupe_attack: Optional[int]
    rainbow_attack: Optional[int]
    base_defence: int
    max_defence: int
    free_dupe_defence: Optional[int]
    rainbow_defence: Optional[int]
    ki_multiplier: str
    transformations: List[Transformation]
    active_skill: Optional[str]
    active_skill_condition: Optional[str]
    eza_leader_skill: Optional[str]
    eza_super_attack: Optional[str]
    eza_ultra_super_attack: Optional[str]
    eza_passive: Optional[str]
    eza_active_skill: Optional[str]
    eza_active_skill_condition: Optional[str]
    transformation_condition: Optional[str]

    def __init__(self, name: str, title: str, max_level: int, max_sa_level: Optional[int], rarity: Rarity, welcome4_class: Optional[Class], type: Optional[TypeEnum], cost: int, id: int, image_url: str, leader_skill: str, super_attack: str, ultra_super_attack: Optional[str], passive: str, links: List[str], categories: List[str], ki_meter: List[KiMeter], base_hp: int, max_level_hp: int, free_dupe_hp: Optional[int], rainbow_hp: Optional[int], base_attack: int, max_level_attack: int, free_dupe_attack: Optional[int], rainbow_attack: Optional[int], base_defence: int, max_defence: int, free_dupe_defence: Optional[int], rainbow_defence: Optional[int], ki_multiplier: str, transformations: List[Transformation], active_skill: Optional[str], active_skill_condition: Optional[str], eza_leader_skill: Optional[str], eza_super_attack: Optional[str], eza_ultra_super_attack: Optional[str], eza_passive: Optional[str], eza_active_skill: Optional[str], eza_active_skill_condition: Optional[str], transformation_condition: Optional[str]) -> None:
        self.name = name
        self.title = title
        self.max_level = max_level
        self.max_sa_level = max_sa_level
        self.rarity = rarity
        self.welcome4_class = welcome4_class
        self.type = type
        self.cost = cost
        self.id = id
        self.image_url = image_url
        self.leader_skill = leader_skill
        self.super_attack = super_attack
        self.ultra_super_attack = ultra_super_attack
        self.passive = passive
        self.links = links
        self.categories = categories
        self.ki_meter = ki_meter
        self.base_hp = base_hp
        self.max_level_hp = max_level_hp
        self.free_dupe_hp = free_dupe_hp
        self.rainbow_hp = rainbow_hp
        self.base_attack = base_attack
        self.max_level_attack = max_level_attack
        self.free_dupe_attack = free_dupe_attack
        self.rainbow_attack = rainbow_attack
        self.base_defence = base_defence
        self.max_defence = max_defence
        self.free_dupe_defence = free_dupe_defence
        self.rainbow_defence = rainbow_defence
        self.ki_multiplier = ki_multiplier
        self.transformations = transformations
        self.active_skill = active_skill
        self.active_skill_condition = active_skill_condition
        self.eza_leader_skill = eza_leader_skill
        self.eza_super_attack = eza_super_attack
        self.eza_ultra_super_attack = eza_ultra_super_attack
        self.eza_passive = eza_passive
        self.eza_active_skill = eza_active_skill
        self.eza_active_skill_condition = eza_active_skill_condition
        self.transformation_condition = transformation_condition
