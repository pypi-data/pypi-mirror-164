import { S as SvelteComponent, i as init, s as safe_not_equal, q as create_component, u as mount_component, v as transition_in, w as transition_out, x as destroy_component, L as assign, M as StatusTracker, V as create_slot, m as space, c as insert, N as get_spread_update, O as get_spread_object, Q as update_slot_base, R as get_all_dirty_from_scope, T as get_slot_changes, e as detach, F as bubble } from './index.230aa104.js';
import { C as Carousel } from './CarouselItem.svelte_svelte_type_style_lang.b72f6d83.js';

/* src/components/Carousel/Carousel.svelte generated by Svelte v3.49.0 */

function create_default_slot(ctx) {
	let statustracker;
	let t;
	let current;
	const statustracker_spread_levels = [/*loading_status*/ ctx[2]];
	let statustracker_props = {};

	for (let i = 0; i < statustracker_spread_levels.length; i += 1) {
		statustracker_props = assign(statustracker_props, statustracker_spread_levels[i]);
	}

	statustracker = new StatusTracker({ props: statustracker_props });
	const default_slot_template = /*#slots*/ ctx[3].default;
	const default_slot = create_slot(default_slot_template, ctx, /*$$scope*/ ctx[5], null);

	return {
		c() {
			create_component(statustracker.$$.fragment);
			t = space();
			if (default_slot) default_slot.c();
		},
		m(target, anchor) {
			mount_component(statustracker, target, anchor);
			insert(target, t, anchor);

			if (default_slot) {
				default_slot.m(target, anchor);
			}

			current = true;
		},
		p(ctx, dirty) {
			const statustracker_changes = (dirty & /*loading_status*/ 4)
			? get_spread_update(statustracker_spread_levels, [get_spread_object(/*loading_status*/ ctx[2])])
			: {};

			statustracker.$set(statustracker_changes);

			if (default_slot) {
				if (default_slot.p && (!current || dirty & /*$$scope*/ 32)) {
					update_slot_base(
						default_slot,
						default_slot_template,
						ctx,
						/*$$scope*/ ctx[5],
						!current
						? get_all_dirty_from_scope(/*$$scope*/ ctx[5])
						: get_slot_changes(default_slot_template, /*$$scope*/ ctx[5], dirty, null),
						null
					);
				}
			}
		},
		i(local) {
			if (current) return;
			transition_in(statustracker.$$.fragment, local);
			transition_in(default_slot, local);
			current = true;
		},
		o(local) {
			transition_out(statustracker.$$.fragment, local);
			transition_out(default_slot, local);
			current = false;
		},
		d(detaching) {
			destroy_component(statustracker, detaching);
			if (detaching) detach(t);
			if (default_slot) default_slot.d(detaching);
		}
	};
}

function create_fragment(ctx) {
	let carousel;
	let current;

	carousel = new Carousel({
			props: {
				elem_id: /*elem_id*/ ctx[0],
				visible: /*visible*/ ctx[1],
				$$slots: { default: [create_default_slot] },
				$$scope: { ctx }
			}
		});

	carousel.$on("change", /*change_handler*/ ctx[4]);

	return {
		c() {
			create_component(carousel.$$.fragment);
		},
		m(target, anchor) {
			mount_component(carousel, target, anchor);
			current = true;
		},
		p(ctx, [dirty]) {
			const carousel_changes = {};
			if (dirty & /*elem_id*/ 1) carousel_changes.elem_id = /*elem_id*/ ctx[0];
			if (dirty & /*visible*/ 2) carousel_changes.visible = /*visible*/ ctx[1];

			if (dirty & /*$$scope, loading_status*/ 36) {
				carousel_changes.$$scope = { dirty, ctx };
			}

			carousel.$set(carousel_changes);
		},
		i(local) {
			if (current) return;
			transition_in(carousel.$$.fragment, local);
			current = true;
		},
		o(local) {
			transition_out(carousel.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			destroy_component(carousel, detaching);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;
	let { elem_id = "" } = $$props;
	let { visible = true } = $$props;
	let { loading_status } = $$props;

	function change_handler(event) {
		bubble.call(this, $$self, event);
	}

	$$self.$$set = $$props => {
		if ('elem_id' in $$props) $$invalidate(0, elem_id = $$props.elem_id);
		if ('visible' in $$props) $$invalidate(1, visible = $$props.visible);
		if ('loading_status' in $$props) $$invalidate(2, loading_status = $$props.loading_status);
		if ('$$scope' in $$props) $$invalidate(5, $$scope = $$props.$$scope);
	};

	return [elem_id, visible, loading_status, slots, change_handler, $$scope];
}

class Carousel_1 extends SvelteComponent {
	constructor(options) {
		super();

		init(this, options, instance, create_fragment, safe_not_equal, {
			elem_id: 0,
			visible: 1,
			loading_status: 2
		});
	}
}

var Carousel_1$1 = Carousel_1;

const modes = ["static"];

export { Carousel_1$1 as Component, modes };
