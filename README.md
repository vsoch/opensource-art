# Open Source Art

[![CircleCI](https://circleci.com/gh/vsoch/opensource-art.svg?style=svg)](https://circleci.com/gh/vsoch/opensource-art)

 - [What is OpenSource Art](#what-is-opensource-art): Read here if you want to learn about the gallery generated and housed here.
 - [Contribute your Work](#contribute-your-work): Contributing your work combines down to adding some files to this repository. If you aren't an artist, you can [post an issue](https://www.github.com/vsoch/opensource-art/issues) and we will help you.
 - [Ask a question](https://www.github.com/vsoch/opensource-art/issues): Have a question? Need some help? We are here for you!

Or jump right in and [View the Gallery](https://vsoch.github.io/opensource-art).

## What is Opensource Art?

While traditionally used for programming, this reposity combines open source development with community artistic contributions to create the first automated, programatically and manually generated gallery.

### Background

There is typically a strong distinction between things that are made by hand, and by machine. 
It's also more likely the case that you see artist work attributed to one or a few individuals - the paintings in your favorite
gallery are done by one individual, or it's perhaps a collaboration between a small group.

Bring in open source. Open source is a powerful framework with under which many eyes can make tiny contributions to develop highly
complex systems. In the context of programming, this means that a group of developers opens up their code base for contributions from
the community, and many eyes on the code squash the bugs. 

## How does this work?

Under this same model, many small artistic contributions can create unexpected beauty.

### 1. The Human Component
The base of the entire gallery, whether it be code that drives its generation or the human hand, starts with a human component. 
How does this work?

 1. Any member of the community can contribute a texture, a graphic, or digital piece. The contribution is done via a pull request (or contact of one of the Open Source Art maintainers, in the case the artist is not familiar with Github).
 2. The contribution (if necessary) can be discussed and reviewed.
 3. The texture is added to the library housed in the repository

### 2. The Digital Gallery

From the human component, we have a version controlled collection of community contributions. Each carries with it metadata about the artist and (if one exists) a title and description. Here is where the machine, and concepts from software engineering like version control, continuous integration, and machine learning come into play! We use these technologies to automate the process of generating new works from the existing.

 4. Each day, a set of textures (or derivations from them) are randomly chosen during an automated testing step in a continuous integration service.
 5. Machine learning is performed via a reproducible container to generate a new work
 6. The new work is saved, and added programatically back to the gallery.

### 3. The Open Source Art Story

Over time, the gallery grows in size and complexity. We generate a new image each day, and so the earlier pieces become part of the later ones. The earliest contributions start the development of a story, and community members can contribute new textures (or similar) at any frequency to continue developing the story.

# Contribute Your Work

Contributing comes down to submission of a [pull request](https://yangsu.github.io/pull-request-tutorial/) (called a PR) to this repository.

### Manual Generation
First, the repository, and clone it to your local computer.

```bash
git clone https://www.github.com/<username>/opensource-art
cd opensource-art
```

Next, copy one of the current works pages under [_works](docs/_works), and give it a unique name that is all lowercase
and doesn't have any special characters. Fill in the very minimal metadata for your contribution. All
fields are optional except for the layout, which you should not change from "work."
Here is a template you can start with:

```
---
layout: work
title:  "Eye Guy Ball"
tagged: awareness, eyeguy, cute
date:   2018-08-08 12:54:46
author: Natacha Sochat
website: http://www.natacha.net
image: 2018/eyeguy-nsochat.jpg
---

You can write a description here, if you like!
```

The image path should be under the root "assets/img" in the repository. Thus for the above:

```bash
2018/eye-guys-sochat.png --> assets/images/2018/eye-guys-sochat.png
```
