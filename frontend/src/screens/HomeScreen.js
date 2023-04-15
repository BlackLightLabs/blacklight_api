import React, {useState, useEffect} from 'react';
import {Container, Row, Col, Card, Image} from 'react-bootstrap';
import './css/HomeScreen.css';
// Framer Motion
import {motion} from "framer-motion"

import  WhatIsBlacklight from '../containers/WhatIsBlacklight'
// Images
import tabular from '../resources/tabular.png';
import new_ds from "../resources/new_ds.png";
import ai from "../resources/ai.png";

function HomeScreen() {
    const [cardsOpacity, setCardsOpacity] = useState(0);
    useEffect(() => {
        const handleScroll = () => {
            const scrollPercentage = window.scrollY / 500;
            console.log(scrollPercentage)
            setCardsOpacity(Math.min(scrollPercentage, 1));
        };

        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, [cardsOpacity]);

    const cardVariants = {
        hidden: {opacity: 0, y: 20},
        visible: {opacity: 1, y: 0},
    };


    return (

        <div className="content-wrapper">

            <div className="title-container">
                <Row className="align-items-center justify-content-center">
                    <Col md={12} xs={12} className="text-center">
                        <motion.h2><b>AUTOMATED</b></motion.h2>
                        <motion.h1><b>MACHINE LEARNING</b></motion.h1>
                        <motion.h1>
                            <b>FOR ALL</b>
                        </motion.h1>
                    </Col>
                </Row>
            </div>
            <div className="cards-section" style={{opacity: cardsOpacity}}>
                <Container className="my-5 card-container" style={{opacity: cardsOpacity}}>
                    <Row className="my-3">
                        <Col md={12}>
                            <motion.div
                                variants={cardVariants}
                                initial="hidden"
                                animate={cardsOpacity === 1 ? "visible" : "hidden"}
                                transition={{duration: 0.5}}
                            >
                                <Card bg={"info"}>
                                    <Card.Header>End-to-End Machine Learning</Card.Header>
                                    <Card.Body>
                                        <Row>
                                            <Col md={6}>
                                                <Card.Text>
                                                    Blacklight Labs specializes in end-to-end machine learning, offering
                                                    a
                                                    unique type-5
                                                    system that interviews the user to figure out how to make a machine
                                                    learning model
                                                    for them.
                                                </Card.Text>
                                            </Col>
                                            <Col md={6}>
                                                <Image src={tabular} alt="Image description"
                                                       className="img-fluid rounded-image"/>
                                            </Col>
                                        </Row>
                                    </Card.Body>
                                </Card>
                            </motion.div>
                        </Col>
                    </Row>
                    <Row className="my-3">
                        <Col md={12}>
                            <motion.div
                                variants={cardVariants}
                                initial="hidden"
                                animate={cardsOpacity === 1 ? "visible" : "hidden"}
                                transition={{duration: 0.5}}
                            >
                                <Card bg={"info"}>
                                    <Card.Header>Tabular and Image Data</Card.Header>
                                    <Card.Body>
                                        <Row>
                                            <Col md={6}>
                                                <Card.Text>
                                                    Blacklight Labs' machine learning system works with tabular and
                                                    image
                                                    data,
                                                    providing a versatile solution for a variety of use cases.
                                                </Card.Text>
                                            </Col>
                                            <Col md={6}>
                                                <Image src={ai} alt="Image description"
                                                       className="img-fluid rounded-image"/>
                                            </Col>
                                        </Row>
                                    </Card.Body>
                                </Card>
                            </motion.div>
                        </Col>
                    </Row>
                    <Row className="my-3">
                        <Col md={12}>
                            <motion.div
                                variants={cardVariants}
                                initial="hidden"
                                animate={cardsOpacity === 1 ? "visible" : "hidden"}
                                transition={{duration: 0.5}}
                            >
                                <Card bg={"info"}>
                                    <Card.Header>Tabular and Image Data</Card.Header>
                                    <Card.Body>
                                        <Row>
                                            <Col md={6}>
                                                <Card.Text>
                                                    Blacklight Labs' system automates the machine learning model
                                                    creation
                                                    process,
                                                    making it easy and accessible for all types of users.
                                                </Card.Text>
                                            </Col>
                                            <Col md={6}>
                                                <Image src={new_ds} alt="Image description"
                                                       className="img-fluid rounded-image"/>
                                            </Col>
                                        </Row>
                                    </Card.Body>
                                </Card>
                            </motion.div>
                        </Col>
                    </Row>

                    <WhatIsBlacklight />
                </Container>

            </div>
        </div>
    );
}

export default HomeScreen;