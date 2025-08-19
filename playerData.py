from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any


# --- Nested domain dataclasses ------------------------------------------------

@dataclass
class Summary:
    composite_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    team: Optional[str] = None
    league: Optional[str] = None
    bats: Optional[str] = None
    throws: Optional[str] = None
    height_inches: Optional[int] = None
    weight_lbs: Optional[int] = None
    recent_headshot: Optional[bytes] = None   # store raw BLOB bytes
    birthday: Optional[str] = None            # keep as ISO string "YYYY-MM-DD" for DB compatibility
    hometown: Optional[str] = None
    awards: Optional[str] = None              # comma-separated or JSON string


@dataclass
class StandardBatting:
    composite_id: Optional[str] = None
    wins_above_replacement: Optional[float] = None
    games: Optional[int] = None
    plate_appearances: Optional[int] = None
    at_bats: Optional[int] = None
    runs_scored: Optional[int] = None
    hits: Optional[int] = None
    doubles: Optional[int] = None
    triples: Optional[int] = None
    home_runs: Optional[int] = None
    runs_batted_in: Optional[int] = None
    stolen_bases: Optional[int] = None
    caught_stealing: Optional[int] = None
    walks: Optional[int] = None
    strike_outs: Optional[int] = None
    batting_average: Optional[float] = None
    on_base_percentage: Optional[float] = None
    slugging: Optional[float] = None
    ops: Optional[float] = None
    ops_plus: Optional[float] = None
    roba: Optional[float] = None
    rbat_plus: Optional[float] = None
    total_bases: Optional[int] = None
    grounded_into_double_plays: Optional[int] = None
    hit_by_pitch: Optional[int] = None
    sacrifice_bunts: Optional[int] = None
    sacrifice_flies: Optional[int] = None
    intentional_walks: Optional[int] = None
    position: Optional[str] = None


@dataclass
class AdvancedBatting:
    composite_id: Optional[str] = None
    babip: Optional[float] = None
    iso: Optional[float] = None
    hr_pct: Optional[float] = None
    so_pct: Optional[float] = None
    bb_pct: Optional[float] = None
    ev: Optional[float] = None
    hard_hit_pct: Optional[float] = None
    ld_pct: Optional[float] = None
    gb_pct: Optional[float] = None
    fb_pct: Optional[float] = None
    gb_fb_ratio: Optional[float] = None
    pull_pct: Optional[float] = None
    center_pct: Optional[float] = None
    oppo_pct: Optional[float] = None
    wpa: Optional[float] = None
    cwpa: Optional[float] = None
    re24: Optional[float] = None
    rs_pct: Optional[float] = None
    sb_pct: Optional[float] = None
    xbt_pct: Optional[float] = None


@dataclass
class ValueBatting:
    composite_id: Optional[str] = None
    PA: Optional[float] = None
    Rbat: Optional[float] = None
    Rbaser: Optional[float] = None
    Rdp: Optional[float] = None
    Rfield: Optional[float] = None
    Rpos: Optional[float] = None
    RAA: Optional[float] = None
    WAA: Optional[float] = None
    Rrep: Optional[float] = None
    RAR: Optional[float] = None
    WAR: Optional[float] = None
    waa_wl_pct: Optional[float] = None
    wl_162: Optional[float] = None
    oWAR: Optional[float] = None
    dWAR: Optional[float] = None
    oRAR: Optional[float] = None


@dataclass
class StandardPitching:
    composite_id: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    win_loss_pct: Optional[float] = None
    era: Optional[float] = None
    games: Optional[int] = None
    games_started: Optional[int] = None
    games_finished: Optional[int] = None
    complete_games: Optional[int] = None
    shutouts: Optional[int] = None
    saves: Optional[int] = None
    innings_pitched: Optional[float] = None
    hits_allowed: Optional[int] = None
    runs_allowed: Optional[int] = None
    earned_runs: Optional[int] = None
    home_runs_allowed: Optional[int] = None
    walks: Optional[int] = None
    intentional_walks: Optional[int] = None
    strike_outs: Optional[int] = None
    hit_by_pitch: Optional[int] = None
    balks: Optional[int] = None
    wild_pitches: Optional[int] = None
    batters_faced: Optional[int] = None
    era_plus: Optional[float] = None
    fip: Optional[float] = None
    whip: Optional[float] = None
    hits_per_9: Optional[float] = None
    hr_per_9: Optional[float] = None
    bb_per_9: Optional[float] = None
    so_per_9: Optional[float] = None
    so_to_bb: Optional[float] = None


@dataclass
class AdvancedPitching:
    composite_id: Optional[str] = None
    innings_pitched: Optional[float] = None
    batting_average: Optional[float] = None
    on_base_percentage: Optional[float] = None
    slugging: Optional[float] = None
    ops: Optional[float] = None
    babip: Optional[float] = None
    hr_pct: Optional[float] = None
    k_pct: Optional[float] = None
    bb_pct: Optional[float] = None
    exit_velocity: Optional[float] = None
    hard_hit_pct: Optional[float] = None
    ld_pct: Optional[float] = None
    gb_pct: Optional[float] = None
    fb_pct: Optional[float] = None
    gb_fb_ratio: Optional[float] = None
    wpa: Optional[float] = None
    cwpa: Optional[float] = None
    re24: Optional[float] = None


@dataclass
class ValuePitching:
    composite_id: Optional[str] = None
    innings_pitched: Optional[float] = None
    games: Optional[int] = None
    games_started: Optional[int] = None
    runs_allowed: Optional[int] = None
    ra9: Optional[float] = None
    ra9_opponent: Optional[float] = None
    ra9_defense: Optional[float] = None
    ra9_role: Optional[float] = None
    ra9_extras: Optional[float] = None
    ppfp: Optional[float] = None
    ra9_avg: Optional[float] = None
    raa: Optional[float] = None
    waa: Optional[float] = None
    waa_adj: Optional[float] = None
    war: Optional[float] = None
    rar: Optional[float] = None
    waa_wl_pct: Optional[float] = None
    wl_162: Optional[float] = None


@dataclass
class StandardFielding:
    composite_id: Optional[str] = None
    position: Optional[str] = None
    games: Optional[int] = None
    games_started: Optional[int] = None
    complete_games: Optional[int] = None
    innings: Optional[float] = None
    chances: Optional[int] = None
    putouts: Optional[int] = None
    assists: Optional[int] = None
    errors: Optional[int] = None
    double_plays: Optional[int] = None
    fielding_percentage: Optional[float] = None
    league_fielding_percentage: Optional[float] = None
    total_zone_total: Optional[float] = None
    total_zone_per_year: Optional[float] = None
    defensive_runs_saved: Optional[float] = None
    defensive_runs_saved_per_year: Optional[float] = None
    range_factor_per_9: Optional[float] = None
    league_range_factor_per_9: Optional[float] = None
    range_factor_per_game: Optional[float] = None
    league_range_factor_per_game: Optional[float] = None
    stolen_bases_allowed: Optional[int] = None
    caught_stealing: Optional[int] = None
    caught_stealing_percentage: Optional[float] = None
    league_caught_stealing_percentage: Optional[float] = None
    pickoffs: Optional[int] = None


@dataclass
class SalaryEntry:
    composite_id: Optional[str] = None
    year: Optional[int] = None
    salary: Optional[float] = None


# --- Top-level PlayerData ----------------------------------------------------

@dataclass
class PlayerData:
    summary: Summary = field(default_factory=Summary)
    standard_batting: StandardBatting = field(default_factory=StandardBatting)
    advanced_batting: AdvancedBatting = field(default_factory=AdvancedBatting)
    value_batting: ValueBatting = field(default_factory=ValueBatting)
    standard_pitching: StandardPitching = field(default_factory=StandardPitching)
    advanced_pitching: AdvancedPitching = field(default_factory=AdvancedPitching)
    value_pitching: ValuePitching = field(default_factory=ValuePitching)
    standard_fielding: StandardFielding = field(default_factory=StandardFielding)
    salary_history: List[SalaryEntry] = field(default_factory=list)

    # --- convenience helpers -------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to plain dict; nested dataclasses are converted to dicts as well.
        Good for JSON serialization (note: recent_headshot bytes must be handled).
        """
        out = {
            "summary": asdict(self.summary),
            "standard_batting": asdict(self.standard_batting),
            "advanced_batting": asdict(self.advanced_batting),
            "value_batting": asdict(self.value_batting),
            "standard_pitching": asdict(self.standard_pitching),
            "advanced_pitching": asdict(self.advanced_pitching),
            "value_pitching": asdict(self.value_pitching),
            "standard_fielding": asdict(self.standard_fielding),
            "salary_history": [asdict(s) for s in self.salary_history],
        }
        return out

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PlayerData":
        """
        Build PlayerData from a nested dict. Useful after reading JSON or DB rows you combined.
        """
        return cls(
            summary=Summary(**(data.get("summary") or {})),
            standard_batting=StandardBatting(**(data.get("standard_batting") or {})),
            advanced_batting=AdvancedBatting(**(data.get("advanced_batting") or {})),
            value_batting=ValueBatting(**(data.get("value_batting") or {})),
            standard_pitching=StandardPitching(**(data.get("standard_pitching") or {})),
            advanced_pitching=AdvancedPitching(**(data.get("advanced_pitching") or {})),
            value_pitching=ValuePitching(**(data.get("value_pitching") or {})),
            standard_fielding=StandardFielding(**(data.get("standard_fielding") or {})),
            salary_history=[SalaryEntry(**s) for s in (data.get("salary_history") or [])],
        )