angular.module('RDash')
    .controller('OrderCtrl', ['OrderService', OrderCtrl]);

function OrderCtrl(OrderService) {
    var self = this
    self.types = ['', 'market', 'limit', 'stop', 'cancel']
    self.type = self.types[0]
    self.statuses = ['', 'finished', 'created', 'cancel']
    self.status = self.statuses[0]
    self.pages = [1,2,3,4,5]
    self.page = self.pages[0]
    
    self.search = function() {
        params = {
            count: 20,
            skip: (self.page - 1) * 20
        }
        if (self.code) {
            params.code = self.code
        }
        if (self.type) {
            params.type = self.type
        }
        if (self.status) {
            params.status = self.status
        }
        OrderService.query(params, function(results) {
            self.orders = results
        })
    }

    self.search()

    self.switchPage = function(index) {
        self.page = self.pages[index]
        self.search()
    }
}