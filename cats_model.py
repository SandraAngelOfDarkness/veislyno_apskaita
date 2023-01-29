from datetime import datetime
from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/cats.db')
Base = declarative_base()

#tevai_vaikai = Table('tevas_vaikas', Base.metadata,
    #Column("id", Integer, primary_key=True),
    #Column("tevas_id", Integer, ForeignKey("tevas.id")),
    #Column("vaikas_id", Integer, ForeignKey("vaikas.id")) 
#)


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    veislynas = Column("Veislynas", String)
    gimimo_data = Column("Gimimo data", DateTime)
    kilmes_salis = Column("Kilmes salis", String)
    lytis = Column("Lytis", String)
    vaikai = relationship("Vaikas", back_populates="tevas")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.veislynas}, {self.gimimo_data}, {self.kilmes_salis}, {self.lytis}"


class Mama(Base):
    __tablename__ = "mama"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    veislynas = Column("Veislynas", String)
    gimimo_data = Column("Gimimo data", DateTime)
    kilmes_salis = Column("Kilmes salis", String)
    lytis = Column("Lytis", String)
    vaikai = relationship("Vaikas", back_populates="mama")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.veislynas}, {self.gimimo_data}, {self.kilmes_salis}, {self.lytis}"


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    veislynas = Column("Veislynas", String)
    gimimo_data = Column("Gimimo data", DateTime)
    kilmes_salis = Column("Kilmes salis", String)
    isvyko_gyventi = Column("Isvyko gyventi", String)
    lytis = Column("Lytis", String)
    tevas_id = Column(Integer, ForeignKey("tevas.id"))
    tevas = relationship("Tevas", back_populates="vaikai")
    mama_id = Column(Integer, ForeignKey("mama.id"))
    mama = relationship("Mama", back_populates="vaikai")
    #tevai = relationship("Tevas", secondary=tevai_vaikai, back_populates="vaikai")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.veislynas}, {self.gimimo_data}, {self.kilmes_salis} {self.isvyko_gyventi}, {self.lytis}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    