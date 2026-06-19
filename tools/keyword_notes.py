from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://index-cn-i-game.com.cn"
SAMPLE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    keyword: str
    url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    content: str = ""
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_note_brief(note: KeywordNote) -> str:
    tag_str = ", ".join(note.tags) if note.tags else "无标签"
    url_str = note.url or "无链接"
    return (
        f"[{note.keyword}] 标签: {tag_str} | 链接: {url_str} | 日期: {note.created_at}"
    )


def format_note_detailed(note: KeywordNote) -> str:
    lines = [
        f"关键词: {note.keyword}",
        f"链接: {note.url or '无'}",
        f"标签: {', '.join(note.tags) if note.tags else '无标签'}",
        f"创建时间: {note.created_at}",
        f"内容:",
    ]
    content_lines = note.content.strip().splitlines()
    if content_lines:
        lines.extend(f"  {line}" for line in content_lines)
    else:
        lines.append("  (无内容)")
    return "\n".join(lines)


def generate_example_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="爱游戏",
            url=SAMPLE_URL,
            tags=["娱乐", "游戏平台"],
            content="这是一个示例笔记，用于展示爱游戏相关的关键词记录。",
        ),
        KeywordNote(
            keyword="游戏开发",
            url="https://dev.example.com",
            tags=["技术", "教程"],
            content="记录游戏开发学习路线与工具链。",
        ),
        KeywordNote(
            keyword="Python数据类",
            tags=["编程", "Python"],
            content="Python dataclass 让数据结构更清晰。",
        ),
    ]


def print_all_notes(notes: List[KeywordNote], detailed: bool = False) -> None:
    print(f"共 {len(notes)} 条笔记\n")
    for i, note in enumerate(notes, 1):
        print(f"--- 笔记 {i} ---")
        if detailed:
            print(format_note_detailed(note))
        else:
            print(format_note_brief(note))
        print()


def search_notes(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    keyword_lower = keyword.lower()
    return [
        note
        for note in notes
        if keyword_lower in note.keyword.lower()
        or keyword_lower in " ".join(note.tags).lower()
        or keyword_lower in note.content.lower()
    ]


def main():
    notes = generate_example_notes()
    print_all_notes(notes, detailed=False)

    print("--- 详细格式 ---")
    print_all_notes(notes, detailed=True)

    print("--- 搜索关键词: 爱游戏 ---")
    results = search_notes(notes, "爱游戏")
    print_all_notes(results)


if __name__ == "__main__":
    main()