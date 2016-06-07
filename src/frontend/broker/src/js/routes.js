'use strict';

/**
 * Route configuration for the RDash module.
 */
angular.module('RDash').config(['$stateProvider', '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {

        // For unmatched routes
        $urlRouterProvider.otherwise('/');

        // Application routes
        $stateProvider
            .state('index', {
                url: '/',
                templateUrl: 'templates/dashboard.html',
                controller: 'HomeCtrl as ctrl'
            })
            .state('order', {
                url: '/order',
                templateUrl: 'templates/order.html',
                controller: 'OrderCtrl as ctrl'
            })
            .state('transaction', {
                url: '/transaction',
                templateUrl: 'templates/transaction.html',
                controller: 'TransactionCtrl as ctrl'
            })
            .state('marketDepth', {
                url: '/marketDepth',
                templateUrl: 'templates/marketDepth.html',
                controller: 'MarketDepthCtrl as ctrl'
            })
            .state('404', {
                url: '/404',
                templateUrl: '404.html'
            })
    }
]);