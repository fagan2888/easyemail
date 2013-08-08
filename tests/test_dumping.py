from StringIO import StringIO

from easyemail import EasyEmail

jinja_template = StringIO("Lorem {{ipsum }}!")
mako_template = StringIO("Lorem ${ipsum}!")

def test_correct_dumping_jinja():
    emj = EasyEmail(['body@of.people'], 'me@home.com', 'Fix up, look sharp')
    emj.load_template(
        None,
        {'ipsum': 'Hello!'},
        ttype="jinja2",
        filelike=jinja_template
    )
    dump = emj.dump()
    assert "Subject: Fix up, look sharp" in dump
    assert "From: me@home.com" in dump
    assert "To: body@of.people" in dump
    assert "Lorem Hello!!" in dump

def test_correct_dumping_mako():
    emm = EasyEmail(['body@of.people'], 'me@home.com', 'Fix up, look sharp')
    emm.load_template(
        None,
        {'ipsum': 'Hello!'},
        ttype="mako",
        filelike=mako_template
    )
    dump = emm.dump()
    assert "Subject: Fix up, look sharp" in dump
    assert "From: me@home.com" in dump
    assert "To: body@of.people" in dump
    assert "Lorem Hello!!" in dump
