#!/usr/bin/python

import os

# for category in categories:
#    os.system('mkdir ' + category)
#    os.system('mkdir ' + category + '/old_url_redirects')

def add_redirect(header):
    return file_text


def extract_header(file_text):
    return ""


class Post():

    def __init__(self, filepath, content):
        self.filepath_instance = filepath
        self.content_instance = content
        self.content_canonical
        self.filepath_canonical
        self.content_instance
        self.filepath_instance
        self._header

    ''' Applies transform behavior

    Parameters
    ==========
    transformBehavior: function
    '''
    def applyTransform(self, transformBehavior):
        self.content_canonical,
        self.filepath_canonical = transformBehavior(self.content_instance,
                                                    self.filepath_instance)

    def save(self):
        open(self.filename_canonical, 'w').write(self.content_canonical)


def transformAddRedirect(content, filepath):

    header = get_header_from_content(content)

    replace_header_value(content)




def applyYamlMappingBehavior(replaceMapping):

    return ""

def get_header_from_content(content):
    header = content[:content.rfind('---') + 3]

    return header

def yamlBehaviorKeep():
    return ""

'''
yamlBehavior = {
    "keep": yamlBehaviorKeep()
}
replaceMapping = {
    "layout": yamlBehavior["keep"],
    "title": yamlBehavior["keep"],
    "author": yamlBehavior["addAuthor"],
    "category": yamlBehavior["replaceCategory"],
    "tags": yamlBehavior["addTags"],
    "use_math": yamlBehavior["keep"],
    "archive": yamlBehavior["keep"],
    "example": yamlBehavior["keep"],
    "excerpt": yamlBehavior["remove"]
}
'''

def split_yaml_and_body_lines(fileLines):

    import numpy as np

    print(np.where(fileLines == "---"))


def main():

    import glob

    os.chdir('_posts/')

    filenames = glob.glob('./**/*.md')

    categories = ['research', 'brewing', 'woodworking', 'hidden',
                  'data-science', 'tech', 'baking']

    for filename in filenames:
        fileLines = open(filename, 'r').readlines()
        for i in range(0, len(fileLines)):
            fileLines[i] = fileLines[i].strip("\n")

        print(fileLines)

        yamlLines, bodyLines = split_yaml_and_body_lines(fileLines)

        print(filename)

        #applyYamlMappingBehavior(lines, )

if __name__ == "__main__":
    main()


'''
    for category in categories:
        if 'category: ' + category in file_text:
            if 0:
                # old url redirect files
                header = file_text[:file_text.rfind('---') + 3]
                url_text = '/' + category + '/' + \
                           filename[:11].replace('-', '/') + \
                           filename[11:].replace('.md', '')
                redirect_text = 'redirect_to: ' + url_text
                header = header.replace('author:', 'author:\n' + redirect_text)
                old_url_filename = category + '/old_url_redirects/' + filename
                open(old_url_filename, 'w').write(header)

            url_text = '/' + \
                       filename[:11].replace('-', '/') + \
                       filename[11:].replace('.md', '') + '/'
            redirect_text = 'redirect_from: ' + url_text
            file_text = file_text.replace('author:', 'author:\n' +
                                          redirect_text)

            # new updated filename
            new_filename = filename.replace(category + '-', '')
            open(filename, 'w').write(file_text)
            os.system('mv ' + filename + ' ' + category + '/' + new_filename)

'''
