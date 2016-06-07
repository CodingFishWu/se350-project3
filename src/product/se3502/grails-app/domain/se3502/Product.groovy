package se3502


import grails.rest.*

@Resource(uri='/product', readOnly = true, formats = ['json', 'xml'])
class Product {
    String name
    String code
    String unit
    String type
}