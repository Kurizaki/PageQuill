"""Core domain models."""

from dataclasses import dataclass
from datetime import date


@dataclass
class GitHubRepository:
    owner: str
    name: str
    default_branch: str


@dataclass
class BlogPost:
    title: str
    slug: str
    date: date
    description: str
    tags: list[str]
    markdown: str
    status: str


@dataclass
class StaticBlogConfig:
    blog_folder: str = "blog"
    posts_folder: str = "blog/posts"
    data_file: str = "blog/data/posts.json"
    theme: str = "minimal"
