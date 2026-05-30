"""
AI Fluency Plan Generator
=========================

Генерирует персональный план AI-грамотности на основе 4D-фреймворка Anthropic:
  - Delegation (делегирование)
  - Description (описание)
  - Discernment (различение)
  - Diligence (тщательность)

Использование:
    python generate_plan.py [--output AI_FLUENCY_PLAN.md]
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Literal

# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

Dimension = Literal["Delegation", "Description", "Discernment", "Diligence"]


@dataclass
class DimensionAssessment:
    """Оценка одного измерения 4D-фреймворка."""

    name: Dimension
    description: str
    current_level: str
    target_level: str


@dataclass
class PhaseActivity:
    """Одна активность внутри фазы плана."""

    week: int
    activity: str
    deliverable: str


@dataclass
class PlanPhase:
    """Фаза плана."""

    title: str
    focus: str
    weeks: str
    activities: list[PhaseActivity] = field(default_factory=list)


@dataclass
class ToolEntry:
    """Запись о инструменте."""

    category: str
    tool: str
    purpose: str


@dataclass
class RiskEntry:
    """Запись о риске."""

    risk: str
    mitigation: str


@dataclass
class AIFluencyPlan:
    """Полный план AI-грамотности."""

    author: str = "Student"
    course: str = "AI Fluency: Framework & Foundations (Anthropic)"
    platform_url: str = (
        "https://anthropic.skilljar.com/ai-fluency-framework-foundations"
    )
    created_date: date = field(default_factory=date.today)
    dimensions: list[DimensionAssessment] = field(default_factory=list)
    phases: list[PlanPhase] = field(default_factory=list)
    tools: list[ToolEntry] = field(default_factory=list)
    success_metrics: list[str] = field(default_factory=list)
    risks: list[RiskEntry] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def default(cls) -> AIFluencyPlan:
        """Создать план с содержимым по умолчанию."""
        plan = cls()

        plan.dimensions = [
            DimensionAssessment(
                name="Delegation",
                description=(
                    "Knowing what to ask AI and when to trust its output"
                ),
                current_level="Intermediate",
                target_level="Advanced",
            ),
            DimensionAssessment(
                name="Description",
                description=(
                    "Crafting clear, precise prompts with context "
                    "and constraints"
                ),
                current_level="Intermediate",
                target_level="Advanced",
            ),
            DimensionAssessment(
                name="Discernment",
                description=(
                    "Critically evaluating AI output for accuracy, "
                    "bias, and completeness"
                ),
                current_level="Beginner",
                target_level="Advanced",
            ),
            DimensionAssessment(
                name="Diligence",
                description=(
                    "Using AI safely, ethically, and sustainably over time"
                ),
                current_level="Intermediate",
                target_level="Advanced",
            ),
        ]

        plan.phases = [
            PlanPhase(
                title="Foundation",
                focus="Delegation & Description",
                weeks="Weeks 1–2",
                activities=[
                    PhaseActivity(
                        1,
                        (
                            "Practice delegating non-coding tasks: "
                            "research summaries, meeting agendas, "
                            "brainstorming"
                        ),
                        "5 documented delegation examples with AI responses",
                    ),
                    PhaseActivity(
                        1,
                        (
                            "Study prompt engineering basics: "
                            "role-setting, context, constraints, "
                            "output format"
                        ),
                        "Prompt template library (markdown)",
                    ),
                    PhaseActivity(
                        2,
                        (
                            "Rewrite 10 of my past prompts using "
                            "the Description framework"
                        ),
                        "Before/after comparison document",
                    ),
                    PhaseActivity(
                        2,
                        (
                            "Experiment with multi-turn conversations "
                            "and iterative refinement"
                        ),
                        "Log of 3 refined multi-turn sessions",
                    ),
                ],
            ),
            PlanPhase(
                title="Critical Thinking",
                focus="Discernment",
                weeks="Weeks 3–4",
                activities=[
                    PhaseActivity(
                        3,
                        (
                            "Fact-check 5 AI-generated responses "
                            "against primary sources"
                        ),
                        "Verification report with discrepancies noted",
                    ),
                    PhaseActivity(
                        3,
                        (
                            "Identify bias in AI outputs "
                            "(tone, assumptions, omissions)"
                        ),
                        "Bias analysis document",
                    ),
                    PhaseActivity(
                        4,
                        (
                            "Practice 'red-teaming' my own prompts: "
                            "ask AI to find flaws in its reasoning"
                        ),
                        "Red-team exercise log",
                    ),
                    PhaseActivity(
                        4,
                        (
                            "Compare outputs across different models "
                            "for the same prompt"
                        ),
                        "Cross-model comparison table",
                    ),
                ],
            ),
            PlanPhase(
                title="Responsible Practice",
                focus="Diligence",
                weeks="Weeks 5–6",
                activities=[
                    PhaseActivity(
                        5,
                        (
                            "Audit my AI usage: what data do I share? "
                            "What do I keep private?"
                        ),
                        "Privacy audit checklist",
                    ),
                    PhaseActivity(
                        5,
                        (
                            "Study AI ethics guidelines "
                            "(Anthropic's Responsible Use)"
                        ),
                        "Summary of key principles",
                    ),
                    PhaseActivity(
                        6,
                        (
                            "Create a personal 'AI usage policy' "
                            "for my projects"
                        ),
                        "Personal policy document",
                    ),
                    PhaseActivity(
                        6,
                        (
                            "Set up a prompt/output journal "
                            "for ongoing reflection"
                        ),
                        "Journal template",
                    ),
                ],
            ),
            PlanPhase(
                title="Integration",
                focus="All 4Ds combined",
                weeks="Weeks 7–8",
                activities=[
                    PhaseActivity(
                        7,
                        (
                            "Apply the full 4D framework to a real "
                            "project end-to-end"
                        ),
                        "Case study document",
                    ),
                    PhaseActivity(
                        7,
                        (
                            "Teach the 4D framework to a colleague "
                            "or friend"
                        ),
                        "Teaching notes / presentation",
                    ),
                    PhaseActivity(
                        8,
                        "Reflect on progress and set long-term goals",
                        "Updated fluency plan (v2)",
                    ),
                    PhaseActivity(
                        8,
                        (
                            "Share learnings in a blog post "
                            "or internal wiki"
                        ),
                        "Published article",
                    ),
                ],
            ),
        ]

        plan.tools = [
            ToolEntry(
                "Primary AI",
                "Claude (Anthropic)",
                "Main assistant for coding, writing, analysis",
            ),
            ToolEntry(
                "Secondary AI",
                "Open-source models (via Ollama)",
                "Comparison and offline use",
            ),
            ToolEntry(
                "Prompt Library",
                "Local markdown files",
                "Reusable prompt templates",
            ),
            ToolEntry(
                "Journal",
                "Obsidian / Notion",
                "Track AI interactions and reflections",
            ),
            ToolEntry(
                "Learning",
                "Anthropic AI Fluency course",
                "Ongoing reference",
            ),
            ToolEntry(
                "Ethics",
                "Anthropic Responsible Use guidelines",
                "Safety checklist",
            ),
        ]

        plan.success_metrics = [
            (
                "Delegation: Confidently ask AI for complex tasks "
                "and get useful results ≥80% of the time."
            ),
            (
                "Description: Prompts include role, context, "
                "constraints, and desired format by default."
            ),
            (
                "Discernment: Verify AI outputs before acting on them, "
                "catching errors in ≥90% of cases."
            ),
            (
                "Diligence: Maintain a weekly AI usage journal "
                "and follow personal policy consistently."
            ),
        ]

        plan.risks = [
            RiskEntry(
                "Over-reliance on AI",
                (
                    "Set 'AI-free' blocks for deep thinking; "
                    "verify critical outputs"
                ),
            ),
            RiskEntry(
                "Privacy leaks",
                (
                    "Never share personal/sensitive data; "
                    "use local models for sensitive work"
                ),
            ),
            RiskEntry(
                "Stale knowledge",
                (
                    "Regularly review AI capabilities "
                    "and update prompt library"
                ),
            ),
            RiskEntry(
                "Burnout",
                "Limit AI usage to focused sessions; take breaks",
            ),
        ]

        return plan

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------

    def to_markdown(self) -> str:
        """Сгенерировать Markdown-представление плана."""
        lines: list[str] = []

        lines.append("# Personal AI Fluency Plan")
        lines.append("")
        lines.append(f"> **Автор:** {self.author}")
        lines.append(f"> **Курс:** {self.course}")
        lines.append(f"> **Платформа:** [Skilljar]({self.platform_url})")
        lines.append(f"> **Дата:** {self.created_date:%Y}")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Section 1: Why
        lines.append("## 1. Why AI Fluency Matters to Me")
        lines.append("")
        lines.append(
            "I work with AI systems daily — from code assistants to "
            "research tools. Yet I noticed a gap: I use AI *intuitively*, "
            "not *strategically*. This course gave me a structured "
            "framework (the **4D Framework**) to turn ad-hoc usage into "
            "deliberate, effective, and safe AI interaction."
        )
        lines.append("")
        lines.append(
            "My goal: become **AI-fluent** — not just a user, but a "
            "thoughtful practitioner who leverages AI responsibly across "
            "work, learning, and personal projects."
        )
        lines.append("")

        # Section 2: 4D Framework
        lines.append("## 2. The 4D AI Fluency Framework — My Understanding")
        lines.append("")
        lines.append(
            "| Dimension | What it means | My current level | Target level |"
        )
        lines.append("|-----------|--------------|------------------|--------------|")
        for d in self.dimensions:
            lines.append(
                f"| **{d.name}** | {d.description} | "
                f"{d.current_level} | {d.target_level} |"
            )
        lines.append("")

        # Section 3: Plan phases
        lines.append("## 3. My Personal AI Fluency Plan")
        lines.append("")
        for phase in self.phases:
            lines.append(f"### Phase: {phase.title} ({phase.weeks})")
            lines.append("")
            lines.append(f"**Focus:** {phase.focus}")
            lines.append("")
            lines.append("| Week | Activity | Deliverable |")
            lines.append("|------|----------|-------------|")
            for act in phase.activities:
                lines.append(
                    f"| {act.week} | {act.activity} | {act.deliverable} |"
                )
            lines.append("")

        # Section 4: Tools
        lines.append("## 4. Tools & Resources")
        lines.append("")
        lines.append("| Category | Tool | Purpose |")
        lines.append("|----------|------|---------|")
        for t in self.tools:
            lines.append(f"| {t.category} | {t.tool} | {t.purpose} |")
        lines.append("")

        # Section 5: Success metrics
        lines.append("## 5. Success Metrics")
        lines.append("")
        lines.append("I will know I'm making progress when:")
        lines.append("")
        for i, metric in enumerate(self.success_metrics, 1):
            lines.append(f"{i}. {metric}")
        lines.append("")

        # Section 6: Risks
        lines.append("## 6. Risks & Mitigations")
        lines.append("")
        lines.append("| Risk | Mitigation |")
        lines.append("|------|-----------|")
        for r in self.risks:
            lines.append(f"| {r.risk} | {r.mitigation} |")
        lines.append("")

        # Section 7: Reflection
        lines.append("## 7. Reflection")
        lines.append("")
        lines.append(
            "> *\"AI fluency isn't about using AI more — "
            "it's about using it better.\"*"
        )
        lines.append("")
        lines.append(
            "This plan is a living document. I will revisit it every "
            "4 weeks and adjust based on what I learn. The 4D framework "
            "gives me a clear lens: every AI interaction is an opportunity "
            "to practice Delegation, Description, Discernment, and Diligence."
        )
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(
            "*Plan version 1.0 — based on Anthropic AI Fluency: "
            "Framework & Foundations course*"
        )
        lines.append("")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Парсинг аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description=(
            "Generate a personal AI Fluency plan based on "
            "Anthropic's 4D framework."
        )
    )
    parser.add_argument(
        "--output",
        type=str,
        default="AI_FLUENCY_PLAN.md",
        help="Output file path (default: AI_FLUENCY_PLAN.md)",
    )
    parser.add_argument(
        "--author",
        type=str,
        default="Student",
        help="Author name (default: Student)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print plan to stdout instead of writing to file",
    )
    return parser.parse_args()


def main() -> None:
    """Точка входа."""
    args = parse_args()

    plan = AIFluencyPlan.default()
    plan.author = args.author

    markdown = plan.to_markdown()

    if args.dry_run:
        print(markdown)
    else:
        out_path = Path(args.output)
        out_path.write_text(markdown, encoding="utf-8")
        print(f"✅ AI Fluency Plan written to {out_path}")
        print(f"   Size: {out_path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
