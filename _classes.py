class DocTemplate(object):
    """Represents a template from which the docs page can be generated
    """

    def __init__(self):
        self.topics = []  #the list of topics that will be display on the page

    def add_topic(self, topic):
        self.topics.append(topic)

    def get_all_section_names(self):
        return [section.display_name
                for topic in self.topics
                for section in topic.sections]

    def get_ordered_topics(self):
        return sorted(self.topics, key=lambda t: t.ordering, reverse=False)

class DocTopic(object):
    """Represents a topic with a display name, link, and a list of sections
    """

    def __init__(self, name, ordering, link):
        self.display_name = name
        self.ordering = ordering
        self.link = link
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def get_section_names(self):
        return [sec.display_name for sec in self.sections]

    def get_section_named(self, name):
        for section in self.sections:
            if section.display_name.lower() == name.lower():  #case-insensitive compare
                return section
        raise NoSuchSectionError(name)

    def get_ordered_sections(self):
        return sorted(self.sections, key=lambda s: s.ordering, reverse=False)


class DocSection(object):
    """Represents a section with a display name and a list of subpages
    """

    def __init__(self, name, ordering, pages):
        self.display_name = name
        self.ordering = ordering
        self.id = "cmdTabContent" + self.display_name.replace(' ', '')
        self.pages = pages

    def add_page(self, page):
        self.pages.append(page)


class NoMetaFileError(Exception):
    """Raised when a meta.md file is not found in a directory
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class NoSuchSectionError(Exception):
    """Raised when a meta.md file specifies a section that is not specified
    in the doc template
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)