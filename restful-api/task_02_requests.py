#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch and print posts from JSONPlaceholder API."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts and save to CSV file."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [{
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        } for post in posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
