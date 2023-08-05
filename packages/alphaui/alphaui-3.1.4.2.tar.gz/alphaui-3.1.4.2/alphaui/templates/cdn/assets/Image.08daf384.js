import { S as SvelteComponent, i as init, s as safe_not_equal, f as element, b as attr, H as src_url_equal, c as insert, n as noop, e as detach } from './index.342fe35e.js';

/* src/components/Dataset/ExampleComponents/Image.svelte generated by Svelte v3.49.0 */

function create_fragment(ctx) {
	let img;
	let img_src_value;

	return {
		c() {
			img = element("img");
			attr(img, "class", "gr-sample-image object-contain h-20 w-20");
			if (!src_url_equal(img.src, img_src_value = /*samples_dir*/ ctx[1] + /*value*/ ctx[0])) attr(img, "src", img_src_value);
		},
		m(target, anchor) {
			insert(target, img, anchor);
		},
		p(ctx, [dirty]) {
			if (dirty & /*samples_dir, value*/ 3 && !src_url_equal(img.src, img_src_value = /*samples_dir*/ ctx[1] + /*value*/ ctx[0])) {
				attr(img, "src", img_src_value);
			}
		},
		i: noop,
		o: noop,
		d(detaching) {
			if (detaching) detach(img);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { value } = $$props;
	let { samples_dir } = $$props;

	$$self.$$set = $$props => {
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
		if ('samples_dir' in $$props) $$invalidate(1, samples_dir = $$props.samples_dir);
	};

	return [value, samples_dir];
}

class Image extends SvelteComponent {
	constructor(options) {
		super();
		init(this, options, instance, create_fragment, safe_not_equal, { value: 0, samples_dir: 1 });
	}
}

var ExampleImage = Image;

export { ExampleImage as E };
