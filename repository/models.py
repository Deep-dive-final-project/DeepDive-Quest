from sqlalchemy import Column, String, BigInteger, ForeignKey, TIMESTAMP, text, Text, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()


class Member(Base):
    __tablename__ = "member"

    member_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

    quests = relationship("Quest", back_populates="member")


class QuestState(enum.Enum):
    SOLVED = "SOLVED"
    UNSOLVED = "UNSOLVED"


class Quest(Base):
    __tablename__ = "quest"

    quest_id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_date = Column(Date, nullable=True)
    answer = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)
    name = Column(String(255), nullable=True)
    state = Column(Enum(QuestState), nullable=True)  # Enum 필드
    member_id = Column(BigInteger, ForeignKey("member.member_id"), nullable=True)

    # 관계 설정 (Member와의 관계)
    member = relationship("Member", back_populates="quests")
