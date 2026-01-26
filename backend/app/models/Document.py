import uuid

from sqlmodel import Field, Relationship, SQLModel

class DocumentBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


# Properties to receive on Document creation
class DocumentCreate(DocumentBase):
    pass


# Properties to receive on Document update
class DocumentUpdate(DocumentBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


# Database model, database table inferred from class name
class Document(DocumentBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False,
    )



# Properties to return via API, id is always required
class DocumentPublic(DocumentBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class DocumentsPublic(SQLModel):
    data: list[DocumentPublic]
    count: int
