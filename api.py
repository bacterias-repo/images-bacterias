import os
import cv2
import numpy as np
import requests
from github import Github

def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def save_to_github(image_path, github_token):
    g = Github(github_token)
    repo = g.get_repo("bacterias-repo/grises_hub")
    with open(image_path, "rb") as f:
        content = f.read()
    repo.create_file(f"images/{image_path}", f"Upload {image_path}", content)

def main():
    image_path = "images/image.jpg"
    gray = convert_to_grayscale(image_path)
    cv2.imwrite(image_path, gray)
    github_token = os.environ["GITHUB_TOKEN"]
    save_to_github(image_path, github_token)

if __name__ == '__main__':
    main()
