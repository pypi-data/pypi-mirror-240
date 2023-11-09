# External Imports
from pydantic import BaseModel, Field


class SimulationParameters(BaseModel):
    nx: int = Field(..., gt=0)
    ny: int = Field(..., gt=0)
    nz: int = Field(..., gt=0)
    dx: float = Field(..., gt=0)
    dy: float = Field(..., gt=0)
    dz: float = Field(..., gt=0)
    wind_speed: float = Field(..., ge=0)
    wind_direction: float = Field(..., ge=0, le=360)
    sim_time: int = Field(..., gt=0)
    auto_kill: int = Field(0, ge=0, le=1)
    num_cpus: int = Field(4, gt=0)
    fuel_flag: int = Field(...)
    ignition_flag: int = Field(...)
    output_time: int = Field(..., gt=0)
    topo_flag: int = Field(...)
    fuel_density: float = Field(None, ge=0)
    fuel_moisture: float = Field(None, ge=0)
    fuel_height: float = Field(None, ge=0)

    # @field_validator("fuel_flag")
    # def validate_fuel_flag(cls, v):
    #     assert v in (1, 3, 4, 5), "fuel_flag must be 1, 3, 4, or 5"
    #     return v
    #
    # @field_validator("topo_flag")
    # def validate_topo_flag(cls, v):
    #     assert v in (0, 5), "topo_flag must be 0 or 5"
    #     return v
    #
    # @field_validator("ignition_flag")
    # def validate_ignition_flag(cls, v):
    #     assert v in (1,
    #                  6), "ignition_flag must be 1 or 6. Future versions may support more options."
    #     return v
    #
    # @field_validator("fuel_density")
    # def validate_fuel_density(cls, v, values):
    #     if values["fuel_flag"] == 1:
    #         assert v is not None, "fuel_density must be specified for fuel_flag=1"
    #     return v
    #
    # @field_validator("fuel_moisture")
    # def validate_fuel_moisture(cls, v, values):
    #     if values["fuel_flag"] == 1:
    #         assert v is not None, "fuel_moisture must be specified for fuel_flag=1"
    #     return v
    #
    # @field_validator("fuel_height")
    # def validate_fuel_height(cls, v, values):
    #     if values["fuel_flag"] == 1:
    #         assert v is not None, "fuel_height must be specified for fuel_flag=1"
    #     return v

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return self.model_dump()

    @classmethod
    def from_fastfuels(
        cls,
        zarray,
        wind_speed,
        wind_direction,
        sim_time,
        auto_kill,
        num_cpus,
        fuel_flag,
        ignition_flag,
        output_time,
        topo_flag,
        fuel_density,
        fuel_moisture,
        fuel_height,
    ):
        return cls(
            nx=zarray.attrs["dx"],
            ny=zarray.attrs["dy"],
            nz=zarray.attrs["dz"],
            dx=zarray.attrs["dx"],
            dy=zarray.attrs["dy"],
            dz=zarray.attrs["dz"],
            wind_speed=wind_speed,
            wind_direction=wind_direction,
            sim_time=sim_time,
            auto_kill=auto_kill,
            num_cpus=num_cpus,
            fuel_flag=fuel_flag,
            ignition_flag=ignition_flag,
            output_time=output_time,
            topo_flag=topo_flag,
            fuel_density=fuel_density,
            fuel_moisture=fuel_moisture,
            fuel_height=fuel_height,
        )
