from pydantic import BaseModel, Field


class News(BaseModel):
    title: str = Field(
        default=...,
        example="New iPhone released!",
        description="Title of the news article"
    )
    link: str = Field(
        default=...,
        example="https://www.example.com",
        description="Link to the news article"
    )
    source: str = Field(
        default=...,
        example="CNN",
        description="Source of the news article"
    )
    img: str = Field(
        default=...,
        example="https://www.example.com/image.jpg",
        description="Image of the news article"
    )
    time: str = Field(
        default=...,
        example="1 day ago",
        description="Time relative to current time when the news was published"
    )

    def dict(self, *args, **kwargs):
        base_dict = super().dict(*args, **kwargs, exclude_none=True, by_alias=True)
        return {k: v for k, v in base_dict.items() if v is not None}
