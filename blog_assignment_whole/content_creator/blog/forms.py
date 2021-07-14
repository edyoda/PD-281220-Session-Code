from django.forms import ModelForm, fields
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your email",
            "text": "Comment"
        }