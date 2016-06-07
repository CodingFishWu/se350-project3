angular.module('RDash')
    .controller('TransactionCtrl', ['TransactionService', TransactionCtrl]);

function TransactionCtrl(TransactionService) {
    var self = this
    self.types=['trade', 'cancel']
    self.type = self.types[0]
    self.pages = [1,2,3,4,5]
    self.page = self.pages[0]
    
    self.search = function() {
        params = {
            type: self.type,
            count: 20,
            skip: (self.page - 1) * 20
        }
        if (self.code) {
            params.code = self.code
        }
        TransactionService.query(params, function(results) {
            self.transactions = results
        })
    }

    self.search()

    self.switchPage = function(index) {
        self.page = self.pages[index]
        self.search()
    }
}