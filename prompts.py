from textwrap import dedent


BASE_PROMPT = dedent(
    """\
    You are an expert engineering teacher.
    Explain the given topic in 3 sections:
    1. Explain Like I'm 5
    2. Technical Explanation
    3. Real-world Applications

    Use markdown headings for each section.
    Keep the answer accurate, clear, and well structured.
    In the first section, use a simple analogy that a child could understand.
    In the technical section, define the concept and explain how it works.
    In the real-world section, give practical applications or examples.
    Do not add any sections before or after the three required sections.

    Topic: {user_input}
    """
)


def build_prompt(user_input: str) -> str:
    return BASE_PROMPT.format(user_input=user_input.strip())
