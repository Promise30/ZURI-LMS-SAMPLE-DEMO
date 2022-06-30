from django.db import models

# Create your models here.
class Question(models.Model):
    # id = models.PrimaryKey(auto_increment=True)   Django automatically does the numbering for us
    question_text = models.CharField(max_length=255)
    question_description = models.CharField(max_length=255, default="Basic Description")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    # number of people who took part in the poll
    # link to a question
    # choice_of_answer (Yes/No)
    # votes
    # id = models.PrimaryKey(auto_increment=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} ---> {self.choice_answer}"
