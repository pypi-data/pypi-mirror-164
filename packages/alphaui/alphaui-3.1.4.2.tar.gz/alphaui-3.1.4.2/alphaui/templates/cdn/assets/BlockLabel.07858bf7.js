import { S as SvelteComponent, i as init, s as safe_not_equal, f as element, q as create_component, m as space, h as text, b as attr, t as toggle_class, c as insert, d as append, u as mount_component, j as set_data, v as transition_in, w as transition_out, e as detach, x as destroy_component } from './index.342fe35e.js';
import { g as get_styles } from './styles.db46e346.js';

/* home/runner/work/gradio/gradio/ui/packages/atoms/src/BlockLabel.svelte generated by Svelte v3.49.0 */

function create_fragment(ctx) {
	let div;
	let span;
	let icon;
	let t0;
	let t1;
	let div_class_value;
	let current;
	icon = new /*Icon*/ ctx[1]({});

	return {
		c() {
			div = element("div");
			span = element("span");
			create_component(icon.$$.fragment);
			t0 = space();
			t1 = text(/*label*/ ctx[0]);
			attr(span, "class", "mr-2 h-[12px] w-[12px] opacity-80");
			attr(div, "class", div_class_value = "absolute left-0 top-0 py-1 px-2 rounded-br-lg shadow-sm text-xs text-gray-500 flex items-center pointer-events-none bg-white z-20 border-b border-r border-gray-100 dark:bg-gray-900 " + /*classes*/ ctx[3]);
			toggle_class(div, "h-0", !/*show_label*/ ctx[2]);
			toggle_class(div, "sr-only", !/*show_label*/ ctx[2]);
		},
		m(target, anchor) {
			insert(target, div, anchor);
			append(div, span);
			mount_component(icon, span, null);
			append(div, t0);
			append(div, t1);
			current = true;
		},
		p(ctx, [dirty]) {
			if (!current || dirty & /*label*/ 1) set_data(t1, /*label*/ ctx[0]);

			if (!current || dirty & /*classes*/ 8 && div_class_value !== (div_class_value = "absolute left-0 top-0 py-1 px-2 rounded-br-lg shadow-sm text-xs text-gray-500 flex items-center pointer-events-none bg-white z-20 border-b border-r border-gray-100 dark:bg-gray-900 " + /*classes*/ ctx[3])) {
				attr(div, "class", div_class_value);
			}

			if (dirty & /*classes, show_label*/ 12) {
				toggle_class(div, "h-0", !/*show_label*/ ctx[2]);
			}

			if (dirty & /*classes, show_label*/ 12) {
				toggle_class(div, "sr-only", !/*show_label*/ ctx[2]);
			}
		},
		i(local) {
			if (current) return;
			transition_in(icon.$$.fragment, local);
			current = true;
		},
		o(local) {
			transition_out(icon.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) detach(div);
			destroy_component(icon);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let classes;
	let { label = null } = $$props;
	let { Icon } = $$props;
	let { show_label = true } = $$props;
	let { disable = false } = $$props;

	$$self.$$set = $$props => {
		if ('label' in $$props) $$invalidate(0, label = $$props.label);
		if ('Icon' in $$props) $$invalidate(1, Icon = $$props.Icon);
		if ('show_label' in $$props) $$invalidate(2, show_label = $$props.show_label);
		if ('disable' in $$props) $$invalidate(4, disable = $$props.disable);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*disable*/ 16) {
			$$invalidate(3, { classes } = get_styles({ label_container: !disable }, ["label_container"]), classes);
		}
	};

	return [label, Icon, show_label, classes, disable];
}

class BlockLabel extends SvelteComponent {
	constructor(options) {
		super();

		init(this, options, instance, create_fragment, safe_not_equal, {
			label: 0,
			Icon: 1,
			show_label: 2,
			disable: 4
		});
	}
}

export { BlockLabel as B };
