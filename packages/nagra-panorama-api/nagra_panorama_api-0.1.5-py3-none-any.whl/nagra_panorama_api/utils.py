# import defusedxml.lxml
import xmltodict
from lxml import etree  # nosec B410

# Safe XML parsing with custom options (solution of the author)
# https://github.com/tiran/defusedxml/issues/102
# Nb: From issue #33, defusedxml.lxml should be depracted by the author.
# PARSER = etree.Parser(remove_blank_text=True, resolve_entities=False)
# LOOKUP = etree.ElementDefaultClassLookup(defusedxml.lxml.RestrictedElement)
# PARSER.set_element_class_lookup(LOOKUP)

# https://stackoverflow.com/questions/3310614/remove-whitespaces-in-xml-string
PARSER = etree.XMLParser(remove_blank_text=True)


def etree_fromstring(string):
    return etree.XML(string, parser=PARSER)


def etree_tostring(element, pretty_print=False):
    return etree_tostring(element, pretty_print=pretty_print)


def parse_response(response):
    if isinstance(response, (str, bytes)):
        # Nb: We should use defusedxml library but it doesn't support
        # Removing blank spaces
        response = etree_fromstring(response)
    data = response.xpath('/response/result/*')
    for d in data:
        detach(d)
    return data


def detach(e):
    parent = e.getparent()
    if parent is not None:
        parent.remove(e)
    return e


def delete_nat_membership(client, ):
    pass


def delete_policy_membership(element):
    entry = element.entry
    # TODO: Check type
    element.remove()  # Remove element from tree
    print(element.dumps(True))
    with entry.as_dict() as d:
        d.target.negate = 'no'
        d['destination-hip'].member = 'any'
    print(element.dumps(True))

    # client.update(e.xpath, e.dumps())
    # client.create(e.xpath, e.dumps())


def map_dicts(a, b):
    """
        Combine values from b with the value in a having the same key.
    """
    for uuid, u in a.items():
        r = b.get(uuid)
        if r is None:
            continue
        yield u, r


def extend_element(dest, elements):
    """
        Only add element that are not already in the destination
        element.extend(...) is causing duplicates entries because
        the merge is not controlled
    """
    children = {c.tag for c in dest.getchildren()}
    for e in elements:
        if e.tag in children:
            continue
        dest.append(e)
    return dest


def el2dict(e):
    return xmltodict.parse(etree_tostring(e))
