#!/usr/env python

import unittest
from subprocess import (
    Popen,
    PIPE,
    STDOUT
)
from glob import glob
import requests
import os
import re
import yaml
import fnmatch
 
here = os.abspath(os.path.dirname(__file__))

# Helper Functions

def recursive_find(base, pattern=None):
    '''recursive find will yield all files in a subdirectory that match a pattern
    '''
    works = []

    if pattern is None:
        pattern = "*"

    for root, dirnames, filenames in os.walk(base):
        for filename in fnmatch.filter(filenames, pattern):
            works.append(os.path.join(root, filename))

    return works

def load_yaml(work):
    metadata = dict()
    with open(work, "r") as stream:
        docs = yaml.load_all(stream)
        for doc in docs:
            if isinstance(doc,dict):
                for k,v in doc.items():
                    print('%s: %s' %(k,v))
                    metadata[k] = v
    return metadata


class TestOpenSourceArt(unittest.TestCase):
 
    def setUp(self):
        self.base = os.path.abspath(os.path.join(here, '../','docs'))
        self.existing = recursive_find('%s/_works' %self.base, '*.md')
        process = Popen(['git','diff-tree','--no-commit-id','--name-only','-r','HEAD'], stderr=PIPE, stdout=PIPE)
        added, error = process.communicate()
        added = [x for x in added.decode('utf-8').split('\n') if x]
        self.added = [x for x in added if x.startswith('_works')] 
        self.lookup = {}
        self.load_works()

    def print_work_name(self, work):
        print('Testing Work %s' % os.path.basename(work).strip('.md'))            

    def load_works(self):
        '''read metadata from newly added works'''
        for work in self.added:
            metadata = dict()
            uid = os.path.basename(work).strip('.md')
            print('Found %s' % uid)

            # Parse the metadata
            if os.path.exists(work):
                metadata = load_yaml(work)
                metadata['uid'] = uid
                self.lookup[work] = metadata
            else:
                print('Skipping %s, file removed.' % registry)

        # Update the list of added
        self.added = list(self.lookup.keys())

    def test_filenames(self):
        for work in self.added:
            self.print_work_name(registry)
            self.assertTrue(work.endswith('md'))
            

    def test_markdown_metadata(self):
        '''ensure that fields are present in markdown file
           layout: work 
           title: Tendrils
           tags: texture
           categories: texture
           date: 2018-08-08 02:54:46
           author: Natacha Sochat
           image: 2018/natacha-sochat-tendrils.jpg
        '''
        print("Checking markdown fields...")

        for work in self.added:

            self.print_work_name(work)
            fields = ['layout',
                      'date',
                      'author',
                      'title',
                      'image',
                      'tags',
                      'categories']
            metadata = self.lookup[work]

            for field in fields:
                self.assertTrue(field in metadata)
                self.assertTrue(metadata[field] not in ['', None])


    def test_images(self):
        ''' ensure that images are:
            1. present in the repository in the right place
            2. named corresponding to the markdown file
            3. jpg or png
        '''
        print("Testing Images for Work")

        for work in self.added:
            self.print_work_name(work)
            metadata = self.lookup[work]

            image_name = metadata['image']
            image_path = '%s/assets/images/%s' % (self.base, image_name)

            # The actual file needs to exist!
            if not os.path.exists(image_path):
                print('ERROR: %s does not exist, reported in %s' %(image_path, 
                                                                   work['uid']))

    def test_generate_output(self):
        '''write to (temporary) file the output of newly added works to generate images for!
           The temporary file is derived from the environment, otherwise put in tmp
           We only make it to this test given that all other tests pass!
        '''

        new_works = os.environ.get('OPENSOURCEART_NEW_WORKS', '/tmp/OSART.new')
        print('New works will be written to %s' %new_works)
        with open(new_works, 'w') as fh:
            for work in self.added:
                fh.writelines('%s\n' %work['image'])

if __name__ == '__main__':
    unittest.main()
