const baseUrl = 'http://104.199.165.224:8000';

angular.module('resources', ['ngResource'])

.factory('UserService', ['$resource', function($resource) {
	return $resource(baseUrl + '/user/:id', {id: '@id'},
	{
		'login': {
			method: 'POST',
			url: baseUrl + '/user/login',
			isArray: false
		}
	});
}])

.factory('OrderService', ['$resource', function($resource) {
	return $resource(baseUrl + '/order/:id', {id: '@id'},
	{

	})
}])

.factory('ProductService', ['$resource', function($resource) {
	return $resource(baseUrl + '/product/:id', {id: '@id'},
	{

	})
}])

.factory('TransactionService', ['$resource', function($resource) {
	return $resource(baseUrl + '/transaction/:id', {id: '@id'},
	{

	})
}])

.factory('MarketDepthService', ['$resource', function($resource) {
	return $resource(baseUrl + '/marketDepth/product/:code', {},
	{
		
	})
}])

.factory('TraderService', ['$resource', function($resource) {
	return $resource(baseUrl + '/trader/:id', {id: '@id'},
	{
		
	})
}])
