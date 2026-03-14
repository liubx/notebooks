"""Template variable generators."""

from datetime import datetime, timedelta
from typing import Dict


class TemplateVariables:
    """Generates common template variables."""
    
    @staticmethod
    def for_daily_note(date: datetime) -> Dict[str, str]:
        """
        Generate variables for daily note template.
        
        Args:
            date: Date for the daily note
        
        Returns:
            Dictionary of template variables
        """
        # Calculate previous and next dates
        prev_date = date - timedelta(days=1)
        next_date = date + timedelta(days=1)
        
        # Day of week in Chinese
        weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        day_of_week = weekdays[date.weekday()]
        
        return {
            'date': date.strftime('%Y-%m-%d'),
            'day_of_week': day_of_week,
            'prev_date': prev_date.strftime('%Y-%m-%d'),
            'next_date': next_date.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_project(
        title: str,
        category: str = 'work',
        start_date: str = '',
        due_date: str = '',
        project_name: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for project template.
        
        Args:
            title: Project title
            category: Project category (work/personal)
            start_date: Project start date (YYYY-MM-DD)
            due_date: Project due date (YYYY-MM-DD)
            project_name: Project name for tags (defaults to title)
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        if not project_name:
            project_name = title
        
        if not start_date:
            start_date = now.strftime('%Y-%m-%d')
        
        return {
            'title': title,
            'category': category,
            'start_date': start_date,
            'due_date': due_date,
            'project_name': project_name,
            'created': now.strftime('%Y-%m-%d'),
            'modified': now.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_meeting(
        title: str,
        date: str = '',
        time: str = '',
        participants: str = '',
        project_tag: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for meeting template.
        
        Args:
            title: Meeting title
            date: Meeting date (YYYY-MM-DD)
            time: Meeting time (HH:MM)
            participants: Comma-separated list of participants
            project_tag: Project tag for the meeting
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        if not date:
            date = now.strftime('%Y-%m-%d')
        
        if not time:
            time = now.strftime('%H:%M')
        
        return {
            'title': title,
            'date': date,
            'time': time,
            'participants': participants,
            'project_tag': project_tag,
            'created': now.strftime('%Y-%m-%d %H:%M:%S'),
            'action_item': '',
            'due_date': '',
            'assignee': '',
        }
    
    @staticmethod
    def for_knowledge_card(
        title: str,
        main_tag: str = '技术',
        source: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for knowledge card template.
        
        Args:
            title: Knowledge card title
            main_tag: Main tag for the card
            source: Source note reference
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        return {
            'title': title,
            'main_tag': main_tag,
            'source': source,
            'created': now.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_adr(
        title: str,
        number: str,
        status: str = '提议'
    ) -> Dict[str, str]:
        """
        Generate variables for ADR template.
        
        Args:
            title: ADR title
            number: ADR number (e.g., '0001')
            status: ADR status (提议/已接受/已废弃)
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        return {
            'title': title,
            'number': number,
            'status': status,
            'date': now.strftime('%Y-%m-%d'),
            'created': now.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_code_snippet(
        title: str,
        language: str,
        code: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for code snippet template.
        
        Args:
            title: Code snippet title
            language: Programming language
            code: Code content
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        # Generate language tag
        language_tag = f'技术/{language}'
        
        return {
            'title': title,
            'language': language,
            'language_tag': language_tag,
            'code': code,
            'created': now.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_problem_solving(
        title: str,
        tech_tag: str = '技术',
        error_message: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for problem solving template.
        
        Args:
            title: Problem title
            tech_tag: Technology tag
            error_message: Error message
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        return {
            'title': title,
            'tech_tag': tech_tag,
            'error_message': error_message,
            'created': now.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_weekly_review(
        year: int,
        week: int,
        date_range: str = '',
        daily_notes_links: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for weekly review template.
        
        Args:
            year: Year
            week: Week number
            date_range: Date range string (e.g., '2024-01-01 ~ 2024-01-07')
            daily_notes_links: Links to daily notes
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        title = f'{year}年第{week}周回顾'
        
        return {
            'title': title,
            'year': str(year),
            'week': str(week).zfill(2),
            'date_range': date_range,
            'daily_notes_links': daily_notes_links,
            'created': now.strftime('%Y-%m-%d'),
        }
    
    @staticmethod
    def for_monthly_review(
        year: int,
        month: int,
        weekly_reviews_links: str = ''
    ) -> Dict[str, str]:
        """
        Generate variables for monthly review template.
        
        Args:
            year: Year
            month: Month
            weekly_reviews_links: Links to weekly reviews
        
        Returns:
            Dictionary of template variables
        """
        now = datetime.now()
        
        title = f'{year}年{month}月回顾'
        
        return {
            'title': title,
            'year': str(year),
            'month': str(month).zfill(2),
            'weekly_reviews_links': weekly_reviews_links,
            'created': now.strftime('%Y-%m-%d'),
        }
