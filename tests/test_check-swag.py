from pages.swag_labs import SwagLabs

def test(browser):

    demopage = SwagLabs(browser)
    demopage.visit()
    assert demopage.exist_icon()
    assert demopage.exist_name()
    assert demopage.exist_password()

