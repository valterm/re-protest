import praw
import json
import csv

def rewrite_comment(comment, new_body):
    comment.edit(new_body)

def save_comments(comments, csv_name, header) -> list:
    with open(csv_name, 'a+', encoding='UTF8') as f:
        ids = []
        writer = csv.writer(f, delimiter=',',quotechar='"')
        reader = csv.reader(f)

        try:
            f_header = next(reader)
            if header != f_header:
                writer.writerow(header)
        except StopIteration:
            writer.writerow(header)

        for id in comments:
            comment = reddit.comment(str(id))
            body = comment.body
            date = comment.created_utc
            score = comment.score
            permalink = comment.permalink

            submission = comment.submission
            title = submission.title

            data = [title, submission, id, date, body, permalink, score]
            writer.writerow(data)

            ids.append(id)
    
    return(ids)

# Set up CSV
header = ['post_title','post_id','comment_id','date_posted','body', 'permalink', 'score']

reddit = praw.Reddit("re-protest-craze4ble", user_agent="test-script-0.1")


user = reddit.user.me()
comments = user.comments.new(limit=None)

ids = save_comments(comments, 'comments.csv', header)
