from __future__ import annotations
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from .models import IssueNature, Issue


class IssueError(Exception):
    def __init__(self, nature: str|Exception, *, on: Model = None, context = None, **kwargs):
        if isinstance(nature, IssueError):
            # Contextualize an IssueError
            self.nature = nature.nature
            self.nature_args = nature.nature_args
            self.on = on or nature.on
            self.context = context or nature.context
            if kwargs:
                raise ValueError("cannot pass kwargs if argument `issue` is already an IssueError")
        
        elif isinstance(nature, Exception):
            self.nature = type(nature).__name__
            self.nature_args = nature.args[0] if len(nature.args) == 1 else nature.args
            self.on = on
            self.context = context
        
        else:
            self.nature = nature
            self.nature_args = kwargs
            self.on = on
            self.context = context

        if self.nature_args and isinstance(self.nature_args, dict):
            message = self.nature.format(**self.nature_args)
        elif self.nature_args:
            message = f"{self.nature}: {self.nature_args}"
        else:
            message = self.nature

        if self.on:
            message += f"\nOn: {self.on}"

        if self.context:
            message += f"\nContext: {self.context}"
        
        super().__init__(message)


    def save(self):
        nature, _ = IssueNature.objects.get_or_create(value=self.nature)
        issue, _ = Issue.objects.update_or_create(nature=nature, nature_args=self.nature_args, on_type=ContentType.objects.get_for_model(self.on), on_id=self.on.pk, defaults={'context': self.context})
        return issue


    DUPLICATE_ITEM_SLUG = 'Duplicate item slug: {slug}'

    @classmethod
    def invalid_type(cls, name: str, actual: type|str, expected: type|str, *, on: Model = None, context = None) -> IssueError:
        if isinstance(actual, type):
            actual = actual.__name__
        if isinstance(expected, type):
            expected = expected.__name__

        return cls("Invalid type for {name}: {actual}, expected {expected}.", name=name, actual=actual, expected=expected, on=on, context=context)


    @classmethod
    def item_not_found_with_id(cls, id: int, *, on: Model = None, context = None) -> IssueError:
        return cls("Item not found with id {id}.", id=id, on=on, context=context)

