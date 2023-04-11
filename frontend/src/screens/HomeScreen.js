import React, {useState, useEffect} from 'react';
import {Container, Row, Col, Card, Image} from 'react-bootstrap';
import './css/HomeScreen.css';
import tabular from '../resources/tabular.png';
import new_ds from "../resources/new_ds.png";
import ai from "../resources/ai.png";

function HomeScreen() {
    const [cardsOpacity, setCardsOpacity] = useState(0);
    useEffect(() => {
        const handleScroll = () => {
            const scrollPercentage = window.scrollY / 325;
            console.log(scrollPercentage)
            setCardsOpacity(Math.min(scrollPercentage, 1));
        };

        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, [cardsOpacity]);

    return (
        <div className="content-wrapper">

            <div className="title-container">
                <Row className="align-items-center justify-content-center">
                    <Col md={12} xs={12} className="text-center">
                        <h2><b>AUTOMATED</b></h2>
                        <h1><b>MACHINE LEARNING</b></h1>
                        <h1><b>FOR ALL</b></h1>
                    </Col>
                </Row>
            </div>
            <div className="cards-section" style={{opacity: cardsOpacity}}>
                <Container className="my-5 card-container" style={{opacity: cardsOpacity}}>
                    <Row className="my-3">
                        <Col md={12}>
                            <Card bg={"info"}>
                                <Card.Header>End-to-End Machine Learning</Card.Header>
                                <Card.Body>
                                    <Row>
                                        <Col md={6}>
                                            <Card.Text>
                                                Blacklight Labs specializes in end-to-end machine learning, offering a
                                                unique type-5
                                                system that interviews the user to figure out how to make a machine
                                                learning model
                                                for them.
                                            </Card.Text>
                                        </Col>
                                        <Col md={6}>
                                            <Image src={tabular} alt="Image description" className="img-fluid rounded-image"/>
                                        </Col>
                                    </Row>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>
                    <Row className="my-3">
                        <Col md={12}>
                            <Card bg={"info"}>
                                <Card.Header>Tabular and Image Data</Card.Header>
                                <Card.Body>
                                    <Row>
                                        <Col md={6}>
                                            <Card.Text>
                                                Blacklight Labs' machine learning system works with tabular and image
                                                data,
                                                providing a versatile solution for a variety of use cases.
                                            </Card.Text>
                                        </Col>
                                        <Col md={6}>
                                            <Image src={ai} alt="Image description" className="img-fluid rounded-image"/>
                                        </Col>
                                    </Row>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>
                    <Row className="my-3">
                        <Col md={12}>
                            <Card bg={"info"}>
                                <Card.Header>Tabular and Image Data</Card.Header>
                                <Card.Body>
                                    <Row>
                                        <Col md={6}>
                                            <Card.Text>
                                                Blacklight Labs' system automates the machine learning model creation
                                                process,
                                                making it easy and accessible for all types of users.
                                            </Card.Text>
                                        </Col>
                                        <Col md={6}>
                                            <Image src={new_ds} alt="Image description" className="img-fluid rounded-image"/>
                                        </Col>
                                    </Row>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>

                </Container>
            </div>
        </div>
    );
}

export default HomeScreen;