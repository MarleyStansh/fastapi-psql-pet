from sqlalchemy.orm import Mapped

from core.models import Base
from core.models.mixins import IntIdPkMixin


class Product(IntIdPkMixin, Base):

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
