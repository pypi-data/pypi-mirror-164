import { S as SvelteComponent, i as init, s as safe_not_equal, V as create_slot, f as element, b as attr, c as insert, Q as update_slot_base, R as get_all_dirty_from_scope, T as get_slot_changes, v as transition_in, w as transition_out, e as detach } from './index.230aa104.js';

var Group_svelte_svelte_type_style_lang = '';

/* src/components/Group/Group.svelte generated by Svelte v3.49.0 */

function create_fragment(ctx) {
	let div;
	let current;
	const default_slot_template = /*#slots*/ ctx[2].default;
	const default_slot = create_slot(default_slot_template, ctx, /*$$scope*/ ctx[1], null);

	return {
		c() {
			div = element("div");
			if (default_slot) default_slot.c();
			attr(div, "class", "svelte-10ogue4");
		},
		m(target, anchor) {
			insert(target, div, anchor);

			if (default_slot) {
				default_slot.m(div, null);
			}

			current = true;
		},
		p(ctx, [dirty]) {
			if (default_slot) {
				if (default_slot.p && (!current || dirty & /*$$scope*/ 2)) {
					update_slot_base(
						default_slot,
						default_slot_template,
						ctx,
						/*$$scope*/ ctx[1],
						!current
						? get_all_dirty_from_scope(/*$$scope*/ ctx[1])
						: get_slot_changes(default_slot_template, /*$$scope*/ ctx[1], dirty, null),
						null
					);
				}
			}
		},
		i(local) {
			if (current) return;
			transition_in(default_slot, local);
			current = true;
		},
		o(local) {
			transition_out(default_slot, local);
			current = false;
		},
		d(detaching) {
			if (detaching) detach(div);
			if (default_slot) default_slot.d(detaching);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;
	let { style = {} } = $$props;

	if (typeof style.mobile_collapse !== "boolean") {
		style.mobile_collapse = true;
	}

	$$self.$$set = $$props => {
		if ('style' in $$props) $$invalidate(0, style = $$props.style);
		if ('$$scope' in $$props) $$invalidate(1, $$scope = $$props.$$scope);
	};

	return [style, $$scope, slots];
}

class Group extends SvelteComponent {
	constructor(options) {
		super();
		init(this, options, instance, create_fragment, safe_not_equal, { style: 0 });
	}
}

var Group$1 = Group;

const modes = ["static"];

export { Group$1 as Component, modes };
