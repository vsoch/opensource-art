# Open Source Art

![docs/assets/logo.jpg](docs/assets/logo.jpg)

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
You can also opt to [fill in an online form](https://vsoch.github.io/opensource-art/contribute) for a manual submission.

### Manual Generation
First, the repository, and clone it to your local computer.

```bash
git clone https://www.github.com/<username>/opensource-art
cd opensource-art
```

## Template

Next, copy one of the current works pages under [_works](docs/_works), and give it a unique name that is all lowercase
and doesn't have any special characters. The following fields have suggestions for their content:

 - *categories* should be one of texture or work.
 - *image* must be defined, as some subfolder path under [assets/images/](docs/assets/images). We recommend that you put the image in the folder for the corresponding year, and that it is named based on `<artist>-<title>.jpg`. We have not tested beyond jpg so we are currently requiring it! (see example below).
 - *layout* you must leave as "work"
 - *tags* are up to you! These should describe your contribution, separated by commas.
 - *date* should be in the format YYYY-MM-DD HH:MM:SS
 - *author* is your name (or alias), although it's not required
 - *affiliation* (not shown in the example) can be your institution, or an affiliation that you have

Here is a template you can start with:

```
---
layout: work
title:  "Circle Packing"
tags: circles, texture, cute
categories: texture
date:   2018-08-08 12:54:46
author: Tim Holman
website: https://generativeartistry.com/tutorials/circle-packing/
image: 2018/tim-holman-circle-packing.jpg
---

You can write a description here, if you like!
```

The image path should be under the root "assets/images" in the repository. Thus for the above:

```bash
2018/tim-holman-circle-packing.jpg --> assets/images/2018/tim-holman-circle-packing.jpg
```

**important** notice that the image name has the **same** unique resource identifier (`tim-holman-circle-packing`) as the post.
This is important for programmatic things, and it will be checked and tested.

Finally, notice that the (more verbose if you like) description is at the bottom, under everything. Feel
free to write as little or as much as you like here.
