"""
Тесты для генератора плана AI-грамотности.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pytest

# Добавляем текущую директорию в sys.path для импорта
sys.path.insert(0, str(Path(__file__).parent))

from generate_plan import (
    AIFluencyPlan,
    Dimension,
    DimensionAssessment,
    PhaseActivity,
    PlanPhase,
    RiskEntry,
    ToolEntry,
)


# ---------------------------------------------------------------------------
# Tests: Data models
# ---------------------------------------------------------------------------

class TestDimensionAssessment:
    """Тесты модели DimensionAssessment."""

    def test_create_delegation(self) -> None:
        d = DimensionAssessment(
            name="Delegation",
            description="Knowing what to ask AI",
            current_level="Beginner",
            target_level="Advanced",
        )
        assert d.name == "Delegation"
        assert d.current_level == "Beginner"
        assert d.target_level == "Advanced"

    def test_all_dimensions(self) -> None:
        dims: list[Dimension] = [
            "Delegation", "Description", "Discernment", "Diligence"
        ]
        for dim in dims:
            d = DimensionAssessment(
                name=dim,
                description="test",
                current_level="Beginner",
                target_level="Advanced",
            )
            assert d.name in dims


class TestPhaseActivity:
    """Тесты модели PhaseActivity."""

    def test_create(self) -> None:
        act = PhaseActivity(
            week=1,
            activity="Study prompt engineering",
            deliverable="Prompt template library",
        )
        assert act.week == 1
        assert "prompt" in act.activity.lower()


class TestPlanPhase:
    """Тесты модели PlanPhase."""

    def test_create_with_activities(self) -> None:
        phase = PlanPhase(
            title="Foundation",
            focus="Delegation & Description",
            weeks="Weeks 1–2",
            activities=[
                PhaseActivity(1, "Activity 1", "Deliverable 1"),
                PhaseActivity(2, "Activity 2", "Deliverable 2"),
            ],
        )
        assert phase.title == "Foundation"
        assert len(phase.activities) == 2


class TestToolEntry:
    """Тесты модели ToolEntry."""

    def test_create(self) -> None:
        t = ToolEntry("Primary AI", "Claude", "Main assistant")
        assert t.category == "Primary AI"
        assert t.tool == "Claude"


class TestRiskEntry:
    """Тесты модели RiskEntry."""

    def test_create(self) -> None:
        r = RiskEntry("Over-reliance", "Set AI-free blocks")
        assert r.risk == "Over-reliance"
        assert "AI-free" in r.mitigation


# ---------------------------------------------------------------------------
# Tests: AIFluencyPlan
# ---------------------------------------------------------------------------

class TestAIFluencyPlan:
    """Тесты основного класса плана."""

    def test_default_has_four_dimensions(self) -> None:
        plan = AIFluencyPlan.default()
        assert len(plan.dimensions) == 4

    def test_default_has_four_phases(self) -> None:
        plan = AIFluencyPlan.default()
        assert len(plan.phases) == 4

    def test_default_has_tools(self) -> None:
        plan = AIFluencyPlan.default()
        assert len(plan.tools) >= 4

    def test_default_has_success_metrics(self) -> None:
        plan = AIFluencyPlan.default()
        assert len(plan.success_metrics) == 4

    def test_default_has_risks(self) -> None:
        plan = AIFluencyPlan.default()
        assert len(plan.risks) >= 3

    def test_default_dimensions_cover_all_4d(self) -> None:
        plan = AIFluencyPlan.default()
        names = [d.name for d in plan.dimensions]
        assert "Delegation" in names
        assert "Description" in names
        assert "Discernment" in names
        assert "Diligence" in names

    def test_default_phases_have_activities(self) -> None:
        plan = AIFluencyPlan.default()
        for phase in plan.phases:
            assert len(phase.activities) >= 2, (
                f"Phase '{phase.title}' should have at least 2 activities"
            )

    def test_to_markdown_contains_title(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "# Personal AI Fluency Plan" in md

    def test_to_markdown_contains_4d_table(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "Delegation" in md
        assert "Description" in md
        assert "Discernment" in md
        assert "Diligence" in md

    def test_to_markdown_contains_phases(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "Foundation" in md
        assert "Critical Thinking" in md
        assert "Responsible Practice" in md
        assert "Integration" in md

    def test_to_markdown_contains_tools_section(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "## 4. Tools & Resources" in md

    def test_to_markdown_contains_success_metrics(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "## 5. Success Metrics" in md

    def test_to_markdown_contains_risks(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "## 6. Risks & Mitigations" in md

    def test_to_markdown_contains_reflection(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert "## 7. Reflection" in md

    def test_to_markdown_is_non_empty(self) -> None:
        plan = AIFluencyPlan.default()
        md = plan.to_markdown()
        assert len(md) > 500  # Plan should be substantial

    def test_author_can_be_customized(self) -> None:
        plan = AIFluencyPlan.default()
        plan.author = "Jane Doe"
        md = plan.to_markdown()
        assert "Jane Doe" in md

    def test_created_date_defaults_to_today(self) -> None:
        plan = AIFluencyPlan.default()
        assert plan.created_date == date.today()

    def test_empty_plan_still_renders(self) -> None:
        """Пустой план должен рендериться без ошибок."""
        plan = AIFluencyPlan()
        md = plan.to_markdown()
        assert "# Personal AI Fluency Plan" in md
        assert len(md) > 0


# ---------------------------------------------------------------------------
# Tests: CLI (dry-run)
# ---------------------------------------------------------------------------

class TestCLI:
    """Тесты командной строки."""

    def test_dry_run_outputs_markdown(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        from generate_plan import main

        # Сохраняем оригинальные аргументы
        original_argv = sys.argv
        try:
            sys.argv = ["generate_plan.py", "--dry-run"]
            main()
            captured = capsys.readouterr()
            assert "# Personal AI Fluency Plan" in captured.out
            assert "Delegation" in captured.out
        finally:
            sys.argv = original_argv

    def test_custom_author(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        from generate_plan import main

        original_argv = sys.argv
        try:
            sys.argv = [
                "generate_plan.py", "--dry-run", "--author", "TestUser"
            ]
            main()
            captured = capsys.readouterr()
            assert "TestUser" in captured.out
        finally:
            sys.argv = original_argv
