angular.module('RDash')
    .controller('MarketDepthCtrl', ['MarketDepthService', MarketDepthCtrl]);

function MarketDepthCtrl(MarketDepthService) {
    var self = this
    self.buys = []
    self.sells = []
    self.search = function() {
        MarketDepthService.query({code: self.code}, function(results) {
            self.marketDepth = results
            for (var i in results) {
                if (results[i].s_b == 'buy') {
                    var flag = true
                    for (var j in self.buys) {
                        if (self.buys[j].price == results[i].price) {
                            self.buys[j].remain += results[i].remain
                            flag = false
                            break
                        }
                    }
                    if (flag) {
                        self.buys.push(results[i])
                    }
                }
                else if (results[i].s_b == 'sell') {
                    var flag = true
                    for (var j in self.sells) {
                        if (self.sells[j].price == results[i].price) {
                            self.sells[j].remain += results[i].remain
                            flag = false
                            break
                        }
                    }
                    if (flag) {
                        self.sells.push(results[i])
                    }
                }
            }
        })
    }
}