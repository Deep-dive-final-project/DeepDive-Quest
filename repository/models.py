from sqlalchemy import Column, String, BigInteger, ForeignKey, Text, Date, Enum, Integer, DECIMAL, TIMESTAMP, DateTime
from sqlalchemy.orm import relationship
from config.database.dbconfig import Base
import enum


class Member(Base):
    __tablename__ = "member"

    member_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

    quests = relationship("Quest", back_populates="member")
    plans = relationship("Plan", back_populates="member")
    tasks = relationship("Task", back_populates="member")

    def __str__(self):
        return f"<Member(id={self.member_id}, name={self.name}, email={self.email}, role={self.role})>"


class Section(Base):
    __tablename__ = "section"

    section_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    sub_section = Column(Text, nullable=True)
    lecture_id = Column(BigInteger, ForeignKey("lecture.lecture_id"), nullable=False)

    lecture = relationship("Lecture", back_populates="sections")
    tasks = relationship("Task", back_populates="section")

    def __str__(self):
        return f"<Section(id={self.section_id}, name={self.name}, lecture_id={self.lecture_id})>"


class Lecture(Base):
    __tablename__ = "lecture"

    lecture_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    instructor = Column(String(100), nullable=True)
    price = Column(Integer, nullable=True)
    rating = Column(DECIMAL(2, 1), nullable=True)
    lecture_url = Column(String(255), nullable=True)
    goals = Column(Text, nullable=True)
    target = Column(Text, nullable=True)
    pre_course = Column(Text, nullable=True)
    platform = Column(String(50), nullable=False)

    sections = relationship("Section", back_populates="lecture")
    plans = relationship("Plan", back_populates="lecture")

    def __str__(self):
        return f"<title={self.title}, goals={self.goals}, target={self.target})>"


class Plan(Base):
    __tablename__ = "plan"

    plan_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    start_date = Column(TIMESTAMP, nullable=True)
    end_date = Column(TIMESTAMP, nullable=True)
    modified_date = Column(TIMESTAMP, nullable=True)
    description = Column(Text, nullable=True)
    state = Column(String(255), nullable=True)
    lecture_id = Column(BigInteger, ForeignKey("lecture.lecture_id", ondelete="CASCADE"), nullable=False)
    member_id = Column(BigInteger, ForeignKey("member.member_id", ondelete="CASCADE"), nullable=False)

    lecture = relationship("Lecture", back_populates="plans")
    member = relationship("Member", back_populates="plans")
    tasks = relationship("Task", back_populates="plan")

    def __str__(self):
        return f"<Plan(id={self.plan_id}, title={self.title})>"


class Task(Base):
    __tablename__ = "task"

    task_id = Column(BigInteger, primary_key=True, autoincrement=True)
    complete_date = Column(DateTime, nullable=True)
    state = Column(String(255), nullable=True)
    title = Column(String(255), nullable=True)
    member_id = Column(BigInteger, ForeignKey("member.member_id", ondelete="CASCADE"), nullable=True)
    plan_id = Column(BigInteger, ForeignKey("plan.plan_id", ondelete="CASCADE"), nullable=True)
    section_id = Column(BigInteger, ForeignKey("section.section_id", ondelete="CASCADE"), nullable=True)

    member = relationship("Member", back_populates="tasks")
    plan = relationship("Plan", back_populates="tasks")
    section = relationship("Section", back_populates="tasks")
    quests = relationship("Quest", back_populates="task")

    def __str__(self):
        return f"<Task(id={self.task_id}, title={self.title})>"


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
    state = Column(Enum(QuestState), nullable=True)
    member_id = Column(BigInteger, ForeignKey("member.member_id"), nullable=False)
    task_id = Column(BigInteger, ForeignKey("task.task_id"), nullable=False)

    member = relationship("Member", back_populates="quests")
    task = relationship("Task", back_populates="quests")

    def __str__(self):
        return f"<Quest(id={self.quest_id}, name={self.name}, state={self.state}, member_id={self.member_id})>"
