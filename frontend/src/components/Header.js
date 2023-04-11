import React from 'react';
import {Navbar, Nav, Container, NavDropDown} from 'react-bootstrap';
import {LinkContainer} from 'react-router-bootstrap';

function Header() {
    return (
        <header>
            <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
                <Container fluid>
                    <LinkContainer to='/'>
                        <Navbar.Brand id={"Logo-text"}> <em>BLACKLIGHT LABS</em></Navbar.Brand>
                    </LinkContainer>
                    <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Container fluid>
                            <Nav className="justify-content-end">
                                <LinkContainer to='/about'>
                                    <Nav.Link>About</Nav.Link>
                                </LinkContainer>
                            </Nav>
                        </Container>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    )
}

export default Header