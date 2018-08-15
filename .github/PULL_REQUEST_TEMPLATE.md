
## Contributor Checklist

Hi Friend! Thanks for contributing an open source art. Please make sure
you check off all the items below!

- [ ] You've added your image as `docs/assets/<year>/<image>.jpg`
- [ ] The image is not greater than 1024px in size (smaller runs faster!)
- [ ] Your metadata post is added with the same `<image>` identifier in `docs/_works/<year>/<image>.md`
- [ ] You have all fields in your metadata file described in [the README](https://github.com/vsoch/opensource-art#template)

Thanks for contributing, the robots can't wait to start working!

### How does this work?

When you create the pull request, it will start a workflow (that will appear below)
on a testing server called "CircleCI" that is going to use a [docker container](https://github.com/vsoch/deepdream-docker)
to generate an artistic piece (well, many!) for the gallery. There are a few steps here:

 - **build** will generate the art pieces, and save them as artifacts for us the preview! You can look at the link for the build step in the workflow and click on "Artifacts" to see them.
 - **update_cache** just saves things for next time.
 - **hold** is a step that requires a manual approval, meaning an administrator of the gallery checks the artifacts, and then gives the good to go!
 - **deploy** sends the images off to the gallery, where they can be appreciated by all.

Feel free to ask questions in the comments below, and let us know if anything is unclear. Thank
you again for your contribution!
