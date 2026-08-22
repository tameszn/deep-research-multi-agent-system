const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set([]),
	mimeTypes: {},
	_: {
		client: {start:"_app/immutable/entry/start.BjZpYW7P.js",app:"_app/immutable/entry/app.DVU2gj2n.js",imports:["_app/immutable/entry/start.BjZpYW7P.js","_app/immutable/chunks/WLsCtw4I.js","_app/immutable/chunks/C0NAgWyT.js","_app/immutable/chunks/CwZQUiQR.js","_app/immutable/entry/app.DVU2gj2n.js","_app/immutable/chunks/C0NAgWyT.js","_app/immutable/chunks/CwZQUiQR.js","_app/immutable/chunks/DjaDRR0M.js","_app/immutable/chunks/Bq9Tj-av.js"],stylesheets:[],fonts:[],uses_env_dynamic_public:false},
		nodes: [
			__memo(() => import('./chunks/0-D8PLqm2g.js')),
			__memo(() => import('./chunks/1-Bzd6iV7l.js')),
			__memo(() => import('./chunks/2-C0uxS_Ck.js').then(function (n) { return n.a0; }))
		],
		remotes: {
			
		},
		routes: [
			{
				id: "/[...catchall]",
				pattern: /^(?:\/([^]*))?\/?$/,
				params: [{"name":"catchall","optional":false,"rest":true,"chained":true}],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		prerendered_routes: new Set([]),
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();

const prerendered = new Set([]);

const base = "";

export { base, manifest, prerendered };
//# sourceMappingURL=manifest.js.map
