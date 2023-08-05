import { S as SvelteComponent, i as init, s as safe_not_equal, f as element, h as text, b as attr, c as insert, d as append, j as set_data, n as noop, e as detach } from './index.230aa104.js';

/* src/components/Dataset/ExampleComponents/Model3D.svelte generated by Svelte v3.49.0 */

function create_fragment(ctx) {
	let div;
	let t;

	return {
		c() {
			div = element("div");
			t = text(/*value*/ ctx[0]);
			attr(div, "class", "gr-sample-3d");
		},
		m(target, anchor) {
			insert(target, div, anchor);
			append(div, t);
		},
		p(ctx, [dirty]) {
			if (dirty & /*value*/ 1) set_data(t, /*value*/ ctx[0]);
		},
		i: noop,
		o: noop,
		d(detaching) {
			if (detaching) detach(div);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { value } = $$props;

	$$self.$$set = $$props => {
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
	};

	return [value];
}

class Model3D extends SvelteComponent {
	constructor(options) {
		super();
		init(this, options, instance, create_fragment, safe_not_equal, { value: 0 });
	}
}

var ExampleModel3D = Model3D;

export { ExampleModel3D as E };
