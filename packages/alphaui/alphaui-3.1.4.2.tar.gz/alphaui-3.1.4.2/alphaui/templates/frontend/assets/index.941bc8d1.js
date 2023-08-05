import { S as SvelteComponent, i as init, s as safe_not_equal, q as create_component, u as mount_component, v as transition_in, w as transition_out, x as destroy_component, V as create_slot, Q as update_slot_base, R as get_all_dirty_from_scope, T as get_slot_changes } from './index.230aa104.js';
import { B as Block } from './Block.67caaa62.js';
import './styles.db46e346.js';

/* src/components/Box/Box.svelte generated by Svelte v3.49.0 */

function create_default_slot(ctx) {
	let current;
	const default_slot_template = /*#slots*/ ctx[3].default;
	const default_slot = create_slot(default_slot_template, ctx, /*$$scope*/ ctx[4], null);

	return {
		c() {
			if (default_slot) default_slot.c();
		},
		m(target, anchor) {
			if (default_slot) {
				default_slot.m(target, anchor);
			}

			current = true;
		},
		p(ctx, dirty) {
			if (default_slot) {
				if (default_slot.p && (!current || dirty & /*$$scope*/ 16)) {
					update_slot_base(
						default_slot,
						default_slot_template,
						ctx,
						/*$$scope*/ ctx[4],
						!current
						? get_all_dirty_from_scope(/*$$scope*/ ctx[4])
						: get_slot_changes(default_slot_template, /*$$scope*/ ctx[4], dirty, null),
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
			if (default_slot) default_slot.d(detaching);
		}
	};
}

function create_fragment(ctx) {
	let block;
	let current;

	block = new Block({
			props: {
				elem_id: /*elem_id*/ ctx[0],
				visible: /*visible*/ ctx[1],
				explicit_call: true,
				$$slots: { default: [create_default_slot] },
				$$scope: { ctx }
			}
		});

	return {
		c() {
			create_component(block.$$.fragment);
		},
		m(target, anchor) {
			mount_component(block, target, anchor);
			current = true;
		},
		p(ctx, [dirty]) {
			const block_changes = {};
			if (dirty & /*elem_id*/ 1) block_changes.elem_id = /*elem_id*/ ctx[0];
			if (dirty & /*visible*/ 2) block_changes.visible = /*visible*/ ctx[1];

			if (dirty & /*$$scope*/ 16) {
				block_changes.$$scope = { dirty, ctx };
			}

			block.$set(block_changes);
		},
		i(local) {
			if (current) return;
			transition_in(block.$$.fragment, local);
			current = true;
		},
		o(local) {
			transition_out(block.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			destroy_component(block, detaching);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;
	let { elem_id } = $$props;
	let { visible = true } = $$props;
	let { style = {} } = $$props;

	if (typeof style.mobile_collapse !== "boolean") {
		style.mobile_collapse = true;
	}

	$$self.$$set = $$props => {
		if ('elem_id' in $$props) $$invalidate(0, elem_id = $$props.elem_id);
		if ('visible' in $$props) $$invalidate(1, visible = $$props.visible);
		if ('style' in $$props) $$invalidate(2, style = $$props.style);
		if ('$$scope' in $$props) $$invalidate(4, $$scope = $$props.$$scope);
	};

	return [elem_id, visible, style, slots, $$scope];
}

class Box extends SvelteComponent {
	constructor(options) {
		super();
		init(this, options, instance, create_fragment, safe_not_equal, { elem_id: 0, visible: 1, style: 2 });
	}
}

var Box$1 = Box;

const modes = ["static"];

export { Box$1 as Component, modes };
