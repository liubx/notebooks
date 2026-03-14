"""Tests for review generator."""

import pytest
from datetime import datetime, timedelta
from pathlib import Path
from hypothesis import given, strategies as st, settings, assume, HealthCheck

from obsidian_km.review import ReviewGenerator
from obsidian_km.config import Config


class TestReviewGenerator:
    """Test review generator functionality."""
    
    def test_get_week_start_date_monday(self, test_vault):
        """Test getting week start date for a Monday."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Monday, January 15, 2024
        date = datetime(2024, 1, 15)
        week_start = generator.get_week_start_date(date)
        
        assert week_start == datetime(2024, 1, 15)
        assert week_start.weekday() == 0  # Monday
    
    def test_get_week_start_date_sunday(self, test_vault):
        """Test getting week start date for a Sunday."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Sunday, January 21, 2024
        date = datetime(2024, 1, 21)
        week_start = generator.get_week_start_date(date)
        
        assert week_start == datetime(2024, 1, 15)
        assert week_start.weekday() == 0  # Monday
    
    def test_get_week_start_date_wednesday(self, test_vault):
        """Test getting week start date for a Wednesday."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Wednesday, January 17, 2024
        date = datetime(2024, 1, 17)
        week_start = generator.get_week_start_date(date)
        
        assert week_start == datetime(2024, 1, 15)
        assert week_start.weekday() == 0  # Monday
    
    def test_get_daily_notes_for_week_empty(self, test_vault):
        """Test getting daily notes for a week with no notes."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        week_start = datetime(2024, 1, 15)
        daily_notes = generator.get_daily_notes_for_week(week_start)
        
        assert daily_notes == []
    
    def test_get_daily_notes_for_week_with_notes(self, test_vault):
        """Test getting daily notes for a week with some notes."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Create some daily notes
        vault = Path(test_vault)
        daily_path = vault / "0-Daily" / "2024" / "01"
        daily_path.mkdir(parents=True, exist_ok=True)
        
        # Create notes for Monday, Wednesday, Friday
        (daily_path / "2024-01-15.md").write_text("Monday note")
        (daily_path / "2024-01-17.md").write_text("Wednesday note")
        (daily_path / "2024-01-19.md").write_text("Friday note")
        
        week_start = datetime(2024, 1, 15)
        daily_notes = generator.get_daily_notes_for_week(week_start)
        
        assert len(daily_notes) == 3
        assert all(note.exists() for note in daily_notes)
    
    def test_get_weekly_review_path(self, test_vault):
        """Test getting weekly review path."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        review_path = generator.get_weekly_review_path(2024, 3)
        
        expected = Path(test_vault) / "0-Daily" / "2024" / "Week-03.md"
        assert review_path == expected
    
    def test_generate_weekly_review(self, test_vault):
        """Test generating a weekly review."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Create some daily notes
        vault = Path(test_vault)
        daily_path = vault / "0-Daily" / "2024" / "01"
        daily_path.mkdir(parents=True, exist_ok=True)
        
        (daily_path / "2024-01-15.md").write_text("Monday note")
        (daily_path / "2024-01-17.md").write_text("Wednesday note")
        
        # Generate review for week containing Jan 15, 2024
        date = datetime(2024, 1, 15)
        review_path = generator.generate_weekly_review(date)
        
        assert review_path.exists()
        assert review_path.name == "Week-03.md"
        
        content = review_path.read_text()
        assert "2024年第3周回顾" in content
        assert "2024-01-15 ~ 2024-01-21" in content
        assert "[[2024-01-15]]" in content
        assert "[[2024-01-17]]" in content
    
    def test_generate_weekly_review_no_daily_notes(self, test_vault):
        """Test generating a weekly review with no daily notes."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        date = datetime(2024, 1, 15)
        review_path = generator.generate_weekly_review(date)
        
        assert review_path.exists()
        
        content = review_path.read_text()
        assert "本周没有日常笔记" in content
    
    def test_get_weekly_reviews_for_month_empty(self, test_vault):
        """Test getting weekly reviews for a month with no reviews."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        weekly_reviews = generator.get_weekly_reviews_for_month(2024, 1)
        
        assert weekly_reviews == []
    
    def test_get_weekly_reviews_for_month_with_reviews(self, test_vault):
        """Test getting weekly reviews for a month with some reviews."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Create some weekly reviews
        vault = Path(test_vault)
        daily_path = vault / "0-Daily" / "2024"
        daily_path.mkdir(parents=True, exist_ok=True)
        
        # January 2024 has weeks 1-5
        (daily_path / "Week-01.md").write_text("Week 1")
        (daily_path / "Week-02.md").write_text("Week 2")
        (daily_path / "Week-03.md").write_text("Week 3")
        (daily_path / "Week-04.md").write_text("Week 4")
        (daily_path / "Week-05.md").write_text("Week 5")
        
        weekly_reviews = generator.get_weekly_reviews_for_month(2024, 1)
        
        assert len(weekly_reviews) == 5
        assert all(review.exists() for review in weekly_reviews)
    
    def test_get_monthly_review_path(self, test_vault):
        """Test getting monthly review path."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        review_path = generator.get_monthly_review_path(2024, 1)
        
        expected = Path(test_vault) / "0-Daily" / "2024" / "2024-01-Review.md"
        assert review_path == expected
    
    def test_generate_monthly_review(self, test_vault):
        """Test generating a monthly review."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        # Create some weekly reviews
        vault = Path(test_vault)
        daily_path = vault / "0-Daily" / "2024"
        daily_path.mkdir(parents=True, exist_ok=True)
        
        (daily_path / "Week-01.md").write_text("Week 1")
        (daily_path / "Week-02.md").write_text("Week 2")
        
        # Generate review for January 2024
        review_path = generator.generate_monthly_review(2024, 1)
        
        assert review_path.exists()
        assert review_path.name == "2024-01-Review.md"
        
        content = review_path.read_text()
        assert "2024年1月回顾" in content
        assert "[[Week-01]]" in content
        assert "[[Week-02]]" in content
    
    def test_generate_monthly_review_no_weekly_reviews(self, test_vault):
        """Test generating a monthly review with no weekly reviews."""
        config = Config(vault_path=test_vault)
        generator = ReviewGenerator(config)
        
        review_path = generator.generate_monthly_review(2024, 1)
        
        assert review_path.exists()
        
        content = review_path.read_text()
        assert "本月没有周回顾" in content


# Feature: obsidian-knowledge-management-workflow, Property 11: 周回顾日期范围链接聚合
@given(
    year=st.integers(min_value=2000, max_value=2099),
    week=st.integers(min_value=1, max_value=53),
    num_notes=st.integers(min_value=0, max_value=7)
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_weekly_review_includes_all_daily_notes(tmp_path_factory, year, week, num_notes):
    """
    Property: For any week start date, the weekly review should include links to all daily notes in that week.
    
    **Validates: Requirements 12.3**
    """
    # Skip invalid week numbers
    try:
        # Get a date in the specified week
        date_str = f"{year}-W{week:02d}-1"
        date = datetime.strptime(date_str, "%Y-W%W-%w")
    except ValueError:
        assume(False)  # Skip invalid week numbers
    
    # Create a temporary vault for this test
    test_vault = tmp_path_factory.mktemp("vault")
    config = Config(vault_path=str(test_vault))
    generator = ReviewGenerator(config)
    
    # Get week start
    week_start = generator.get_week_start_date(date)
    
    # Create daily notes for the week
    created_notes = []
    
    for i in range(num_notes):
        note_date = week_start + timedelta(days=i)
        daily_path = test_vault / "0-Daily" / str(note_date.year) / f"{note_date.month:02d}"
        daily_path.mkdir(parents=True, exist_ok=True)
        
        note_path = daily_path / f"{note_date.strftime('%Y-%m-%d')}.md"
        note_path.write_text(f"Note for {note_date}")
        created_notes.append(note_date.strftime('%Y-%m-%d'))
    
    # Generate weekly review
    review_path = generator.generate_weekly_review(date)
    
    # Verify all daily notes are linked
    content = review_path.read_text()
    
    for note_date_str in created_notes:
        assert f"[[{note_date_str}]]" in content


# Feature: obsidian-knowledge-management-workflow, Property 12: 月回顾日期范围链接聚合
@given(
    year=st.integers(min_value=2000, max_value=2099),
    month=st.integers(min_value=1, max_value=12)
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_monthly_review_includes_all_weekly_reviews(tmp_path_factory, year, month):
    """
    Property: For any year and month, the monthly review should include links to all weekly reviews in that month.
    
    **Validates: Requirements 12.4**
    """
    # Create a temporary vault for this test
    test_vault = tmp_path_factory.mktemp("vault")
    config = Config(vault_path=str(test_vault))
    generator = ReviewGenerator(config)
    
    # Get first and last day of the month
    first_day = datetime(year, month, 1)
    if month == 12:
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(year, month + 1, 1) - timedelta(days=1)
    
    # Get ISO week numbers for the month
    first_week_year, first_week, _ = first_day.isocalendar()
    last_week_year, last_week, _ = last_day.isocalendar()
    
    # Create weekly reviews for all weeks in the month
    created_weeks = []
    
    # Handle year boundary cases
    if month == 1 and first_week > 50:
        # January might include week 52/53 of previous year
        daily_path_prev = test_vault / "0-Daily" / str(year - 1)
        daily_path_prev.mkdir(parents=True, exist_ok=True)
        
        # Create week in previous year
        review_path = daily_path_prev / f"Week-{first_week:02d}.md"
        review_path.write_text(f"Week {first_week}")
        created_weeks.append(f"Week-{first_week:02d}")
        
        # Create weeks in current year
        daily_path = test_vault / "0-Daily" / str(year)
        daily_path.mkdir(parents=True, exist_ok=True)
        
        for week_num in range(1, last_week + 1):
            review_path = daily_path / f"Week-{week_num:02d}.md"
            review_path.write_text(f"Week {week_num}")
            created_weeks.append(f"Week-{week_num:02d}")
    elif month == 12 and last_week == 1:
        # December might include week 1 of next year
        daily_path = test_vault / "0-Daily" / str(year)
        daily_path.mkdir(parents=True, exist_ok=True)
        
        for week_num in range(first_week, 54):
            review_path = daily_path / f"Week-{week_num:02d}.md"
            review_path.write_text(f"Week {week_num}")
            created_weeks.append(f"Week-{week_num:02d}")
        
        # Create week 1 in next year
        daily_path_next = test_vault / "0-Daily" / str(year + 1)
        daily_path_next.mkdir(parents=True, exist_ok=True)
        
        review_path = daily_path_next / "Week-01.md"
        review_path.write_text("Week 1")
        created_weeks.append("Week-01")
    else:
        # Normal case - all weeks in the same year
        daily_path = test_vault / "0-Daily" / str(year)
        daily_path.mkdir(parents=True, exist_ok=True)
        
        for week_num in range(first_week, last_week + 1):
            review_path = daily_path / f"Week-{week_num:02d}.md"
            review_path.write_text(f"Week {week_num}")
            created_weeks.append(f"Week-{week_num:02d}")
    
    # Generate monthly review
    review_path = generator.generate_monthly_review(year, month)
    
    # Verify all weekly reviews are linked
    content = review_path.read_text()
    
    for week_name in created_weeks:
        assert f"[[{week_name}]]" in content


# Feature: obsidian-knowledge-management-workflow, Property 13: 回顾文件路径生成
@given(
    year=st.integers(min_value=2000, max_value=2099),
    week=st.integers(min_value=1, max_value=53)
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_weekly_review_stored_in_correct_path(tmp_path_factory, year, week):
    """
    Property: For any weekly review, it should be stored in the correct path (0-Daily/YYYY/Week-WW.md).
    
    **Validates: Requirements 12.5**
    """
    # Skip invalid week numbers
    try:
        date_str = f"{year}-W{week:02d}-1"
        date = datetime.strptime(date_str, "%Y-W%W-%w")
    except ValueError:
        assume(False)
    
    # Create a temporary vault for this test
    test_vault = tmp_path_factory.mktemp("vault")
    config = Config(vault_path=str(test_vault))
    generator = ReviewGenerator(config)
    
    # Generate weekly review
    review_path = generator.generate_weekly_review(date)
    
    # Get the actual ISO week from the date
    actual_year, actual_week, _ = date.isocalendar()
    
    # Verify path format
    expected_path = test_vault / "0-Daily" / str(actual_year) / f"Week-{actual_week:02d}.md"
    
    assert review_path == expected_path
    assert review_path.exists()
    assert review_path.parent.name == str(actual_year)
    assert review_path.parent.parent.name == "0-Daily"


# Feature: obsidian-knowledge-management-workflow, Property 13: 回顾文件路径生成
@given(
    year=st.integers(min_value=2000, max_value=2099),
    month=st.integers(min_value=1, max_value=12)
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_monthly_review_stored_in_correct_path(tmp_path_factory, year, month):
    """
    Property: For any monthly review, it should be stored in the correct path (0-Daily/YYYY/YYYY-MM-Review.md).
    
    **Validates: Requirements 12.5**
    """
    # Create a temporary vault for this test
    test_vault = tmp_path_factory.mktemp("vault")
    config = Config(vault_path=str(test_vault))
    generator = ReviewGenerator(config)
    
    # Generate monthly review
    review_path = generator.generate_monthly_review(year, month)
    
    # Verify path format
    expected_path = test_vault / "0-Daily" / str(year) / f"{year}-{month:02d}-Review.md"
    
    assert review_path == expected_path
    assert review_path.exists()
    assert review_path.parent.name == str(year)
    assert review_path.parent.parent.name == "0-Daily"
