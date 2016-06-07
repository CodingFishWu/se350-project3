/**
 * Master Controller
 */

angular.module('RDash')
    .controller('HomeCtrl', ['TraderService', 'TransactionService', HomeCtrl]);

function HomeCtrl(TraderService, TransactionService) {
    /**
     * Sidebar Toggle & Cookie Control
     */
    var self = this
    self.traders = TraderService.query()
    TransactionService.query({type: 'trade'}, function(results) {
        self.transactions = results
    })
}