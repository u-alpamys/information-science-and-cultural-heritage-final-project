<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0">

    <xsl:output method="html" encoding="UTF=-8" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com"/>
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
                <link href="https://fonts.googleapis.com/css2?family=Akt:wght@100..900&amp;display=swap" rel="stylesheet"/>
                <meta charset="UTF-8"/>
                <title>Pulp Fiction</title>
                <style>
                    body {
                        font-family: "Akt", sans-serif;
                        font-optical-sizing: auto;
                        font-weight: 400;
                        font-style: normal;
                        max-width: 720px;
                        margin: 40px auto;
                        line-height: 1.6;
                        color: #333;
                    }
                    .persName {
                        background-color: #FFF3B0;
                    }
                    .placeName {
                        background-color: #C8F0C8;
                    }
                    .orgName {
                        background-color: #C5E8F7;
                    }
                    .term {
                        background-color: #EDD9F0;
                    }
                    .bibl {
                        background-color: #FFD9C8;
                    }
                    .tooltip {
                        margin-bottom: 20px;
                        padding: 10px;
                        border: 1px solid #ddd;
                    }
                    .tooltip span {
                        margin-right: 15px;
                        padding: 2px 6px;
                    }
                </style>
            </head>
            <body>
                <xsl:apply-templates select="//tei:body"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="tei:title">
        <i><xsl:apply-templates/></i>
    </xsl:template>

    <xsl:template match="tei:persName">
        <span class="persName" title="{@ref}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:placeName">
        <span class="placeName" title="{@ref}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:orgName">
        <span class="orgName" title="{@ref}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:term">
        <span class="term" title="{@ref}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:bibl">
        <span class="bibl" title="{@ref}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="tei:p">
        <p><xsl:apply-templates/></p>
    </xsl:template>

    <xsl:template match="tei:div">
        <div><xsl:apply-templates/></div>
    </xsl:template>

    <xsl:template match="tei:head">
        <h2><xsl:apply-templates/></h2>
    </xsl:template>

</xsl:stylesheet>