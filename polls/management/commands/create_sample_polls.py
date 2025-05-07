from django.core.management.base import BaseCommand
from polls.models import Poll, Choice
from django.utils import timezone

class Command(BaseCommand):
    help = 'Creates sample polls for testing'

    def handle(self, *args, **kwargs):
        # Sample Poll 1: Favorite Programming Language
        poll1 = Poll.objects.create(
            question="What's your favorite programming language?",
            pub_date=timezone.now(),
            active=True
        )
        Choice.objects.bulk_create([
            Choice(poll=poll1, choice_text="Python", votes=0),
            Choice(poll=poll1, choice_text="JavaScript", votes=0),
            Choice(poll=poll1, choice_text="Java", votes=0),
            Choice(poll=poll1, choice_text="C++", votes=0),
        ])

        # Sample Poll 2: Best Web Framework
        poll2 = Poll.objects.create(
            question="Which web framework do you prefer?",
            pub_date=timezone.now(),
            active=True
        )
        Choice.objects.bulk_create([
            Choice(poll=poll2, choice_text="Django", votes=0),
            Choice(poll=poll2, choice_text="React", votes=0),
            Choice(poll=poll2, choice_text="Vue.js", votes=0),
            Choice(poll=poll2, choice_text="Angular", votes=0),
        ])

        # Sample Poll 3: Preferred Development Environment
        poll3 = Poll.objects.create(
            question="What's your preferred development environment?",
            pub_date=timezone.now(),
            active=True
        )
        Choice.objects.bulk_create([
            Choice(poll=poll3, choice_text="VS Code", votes=0),
            Choice(poll=poll3, choice_text="PyCharm", votes=0),
            Choice(poll=poll3, choice_text="Sublime Text", votes=0),
            Choice(poll=poll3, choice_text="Vim/Neovim", votes=0),
        ])

        self.stdout.write(self.style.SUCCESS('Successfully created sample polls')) 