"""Review generator for weekly and monthly reviews."""

from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

from obsidian_km.config import Config
from obsidian_km.templates import TemplateLoader, TemplateVariables


class ReviewGenerator:
    """Generates weekly and monthly reviews."""
    
    def __init__(self, config: Config):
        """
        Initialize review generator.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.vault_path = Path(config.vault_path)
        self.template_loader = TemplateLoader(config.templates_path)
    
    def get_week_start_date(self, date: datetime) -> datetime:
        """
        Get the Monday of the week containing the given date (ISO 8601).
        
        Args:
            date: Any date in the week
        
        Returns:
            Monday of that week
        """
        # ISO 8601: Monday is 0, Sunday is 6
        days_since_monday = date.weekday()
        monday = date - timedelta(days=days_since_monday)
        return monday.replace(hour=0, minute=0, second=0, microsecond=0)
    
    def get_daily_notes_for_week(self, week_start: datetime) -> List[Path]:
        """
        Get all daily notes for a given week (Monday to Sunday).
        
        Args:
            week_start: Monday of the week
        
        Returns:
            List of paths to daily notes that exist
        """
        daily_notes = []
        
        for i in range(7):  # Monday to Sunday
            date = week_start + timedelta(days=i)
            year = date.year
            month = date.month
            date_str = date.strftime('%Y-%m-%d')
            
            note_path = self.vault_path / self.config.daily_notes_path / str(year) / f"{month:02d}" / f"{date_str}.md"
            
            if note_path.exists():
                daily_notes.append(note_path)
        
        return daily_notes
    
    def get_weekly_review_path(self, year: int, week: int) -> Path:
        """
        Get the path for a weekly review.
        
        Args:
            year: Year
            week: ISO week number
        
        Returns:
            Path to the weekly review file
        """
        return self.vault_path / self.config.daily_notes_path / str(year) / f"Week-{week:02d}.md"
    
    def generate_weekly_review(
        self,
        date: Optional[datetime] = None
    ) -> Path:
        """
        Generate a weekly review for the week containing the given date.
        
        Args:
            date: Any date in the week (defaults to today)
        
        Returns:
            Path to the created weekly review
        """
        if date is None:
            date = datetime.now()
        
        # Get week start (Monday)
        week_start = self.get_week_start_date(date)
        week_end = week_start + timedelta(days=6)
        
        # Get ISO week number
        year, week, _ = date.isocalendar()
        
        # Collect daily notes for this week
        daily_notes = self.get_daily_notes_for_week(week_start)
        
        # Generate links to daily notes
        daily_notes_links = self._generate_daily_notes_links(daily_notes)
        
        # Generate date range string
        date_range = f"{week_start.strftime('%Y-%m-%d')} ~ {week_end.strftime('%Y-%m-%d')}"
        
        # Generate variables
        variables = TemplateVariables.for_weekly_review(
            year=year,
            week=week,
            date_range=date_range,
            daily_notes_links=daily_notes_links
        )
        
        # Apply template
        review_content = self.template_loader.apply_template("weekly-review", variables)
        
        # Get review path
        review_path = self.get_weekly_review_path(year, week)
        
        # Create parent directories if needed
        review_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write review
        review_path.write_text(review_content, encoding='utf-8')
        
        return review_path
    
    def _generate_daily_notes_links(self, daily_notes: List[Path]) -> str:
        """
        Generate markdown links to daily notes.
        
        Args:
            daily_notes: List of daily note paths
        
        Returns:
            Markdown formatted links
        """
        if not daily_notes:
            return "本周没有日常笔记"
        
        links = []
        for note_path in daily_notes:
            # Extract date from filename (YYYY-MM-DD.md)
            date_str = note_path.stem
            links.append(f"- [[{date_str}]]")
        
        return "\n".join(links)
    
    def get_weekly_reviews_for_month(self, year: int, month: int) -> List[Path]:
        """
        Get all weekly reviews for a given month.
        
        Args:
            year: Year
            month: Month (1-12)
        
        Returns:
            List of paths to weekly reviews that exist
        """
        weekly_reviews = []
        
        # Get first and last day of the month
        first_day = datetime(year, month, 1)
        if month == 12:
            last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = datetime(year, month + 1, 1) - timedelta(days=1)
        
        # Get ISO week numbers for the month
        first_week = first_day.isocalendar()[1]
        last_week = last_day.isocalendar()[1]
        
        # Handle year boundary (December/January)
        if month == 12 and last_week == 1:
            # December might include week 1 of next year
            for week in range(first_week, 54):  # Up to week 53
                review_path = self.get_weekly_review_path(year, week)
                if review_path.exists():
                    weekly_reviews.append(review_path)
            # Check week 1 of next year
            review_path = self.get_weekly_review_path(year + 1, 1)
            if review_path.exists():
                weekly_reviews.append(review_path)
        elif month == 1 and first_week > 50:
            # January might include week 52/53 of previous year
            review_path = self.get_weekly_review_path(year - 1, first_week)
            if review_path.exists():
                weekly_reviews.append(review_path)
            for week in range(1, last_week + 1):
                review_path = self.get_weekly_review_path(year, week)
                if review_path.exists():
                    weekly_reviews.append(review_path)
        else:
            # Normal case
            for week in range(first_week, last_week + 1):
                review_path = self.get_weekly_review_path(year, week)
                if review_path.exists():
                    weekly_reviews.append(review_path)
        
        return weekly_reviews
    
    def get_monthly_review_path(self, year: int, month: int) -> Path:
        """
        Get the path for a monthly review.
        
        Args:
            year: Year
            month: Month (1-12)
        
        Returns:
            Path to the monthly review file
        """
        return self.vault_path / self.config.daily_notes_path / str(year) / f"{year}-{month:02d}-Review.md"
    
    def generate_monthly_review(
        self,
        year: Optional[int] = None,
        month: Optional[int] = None
    ) -> Path:
        """
        Generate a monthly review for the given year and month.
        
        Args:
            year: Year (defaults to current year)
            month: Month (defaults to current month)
        
        Returns:
            Path to the created monthly review
        """
        now = datetime.now()
        if year is None:
            year = now.year
        if month is None:
            month = now.month
        
        # Collect weekly reviews for this month
        weekly_reviews = self.get_weekly_reviews_for_month(year, month)
        
        # Generate links to weekly reviews
        weekly_reviews_links = self._generate_weekly_reviews_links(weekly_reviews)
        
        # Generate variables
        variables = TemplateVariables.for_monthly_review(
            year=year,
            month=month,
            weekly_reviews_links=weekly_reviews_links
        )
        
        # Apply template
        review_content = self.template_loader.apply_template("monthly-review", variables)
        
        # Get review path
        review_path = self.get_monthly_review_path(year, month)
        
        # Create parent directories if needed
        review_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write review
        review_path.write_text(review_content, encoding='utf-8')
        
        return review_path
    
    def _generate_weekly_reviews_links(self, weekly_reviews: List[Path]) -> str:
        """
        Generate markdown links to weekly reviews.
        
        Args:
            weekly_reviews: List of weekly review paths
        
        Returns:
            Markdown formatted links
        """
        if not weekly_reviews:
            return "本月没有周回顾"
        
        links = []
        for review_path in weekly_reviews:
            # Extract week info from filename (Week-WW.md)
            filename = review_path.stem
            links.append(f"- [[{filename}]]")
        
        return "\n".join(links)
