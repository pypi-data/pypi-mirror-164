from sqlalchemy import Column, Integer, TIMESTAMP, Float, text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
# metadata = Base.metadata


class TbMarchatriskValidationReport(Base):
    __tablename__ = 'tb_marchatrisk_validation_report'

    pk_id = Column(Integer, primary_key=True)
    customer_id = Column(VARCHAR(20))
    model_id = Column(VARCHAR(20))
    training_id = Column(VARCHAR(20))
    source_start_date = Column(VARCHAR(20))
    source_end_date = Column(VARCHAR(20))
    model_name = Column(VARCHAR(100))
    training_sample_count = Column(Integer)
    validation_sample_count = Column(Integer)
    accuracy = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    f1_score = Column(Float)
    marchatrisk_weight = Column(Float)
    marchatrisk_accuracy = Column(Float)
    marchatrisk_precision = Column(Float)
    marchatrisk_recall = Column(Float)
    marchatrisk_f1_score = Column(Float)
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP(6)"))
