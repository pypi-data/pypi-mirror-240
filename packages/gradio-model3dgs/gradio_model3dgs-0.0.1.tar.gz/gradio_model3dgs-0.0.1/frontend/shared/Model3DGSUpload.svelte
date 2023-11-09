<script lang="ts">
	import { createEventDispatcher, tick, onMount } from "svelte";
	import { Upload, ModifyUpload } from "@gradio/upload";
	import type { FileData } from "@gradio/client";
	import { BlockLabel } from "@gradio/atoms";
	import { File } from "@gradio/icons";
	import * as SPLAT from "gsplat";

	export let value: null | FileData;
	export let label = "";
	export let show_label: boolean;
	export let root: string;
	export let i18n: I18nFormatter;

	let mounted = false;
	let canvas: HTMLCanvasElement;
	let scene: SPLAT.Scene | null;

	function reset_scene(): void {
		scene = new SPLAT.Scene();
	}

	onMount(() => {
		scene = new SPLAT.Scene();
		mounted = true;
	});

	$: ({ path } = value || {
		path: undefined
	});

	$: canvas && mounted && path != null && reset_scene();

	async function handle_upload({
		detail
	}: CustomEvent<FileData>): Promise<void> {
		value = detail;
		await tick();
		reset_scene();
		dispatch("change", value);
	}

	async function handle_clear(): Promise<void> {
		scene = null;
		value = null;
		await tick();
		dispatch("clear");
	}

	const dispatch = createEventDispatcher<{
		change: FileData | null;
		clear: undefined;
		drag: boolean;
	}>();

	let dragging = false;

	import type { I18nFormatter } from "@gradio/utils";

	$: dispatch("drag", dragging);
</script>

<BlockLabel {show_label} Icon={File} label={label || "Splat"} />

{#if value === null}
	<Upload
		on:load={handle_upload}
		{root}
		filetype=".ply, .splat"
		bind:dragging
	>
		<slot />
	</Upload>
{:else}
	<div class="input-model">
		<ModifyUpload
			on:clear={handle_clear}
			{i18n}
			absolute
		/>
		<canvas bind:this={canvas} />
	</div>
{/if}

<style>
	.input-model {
		display: flex;
		position: relative;
		justify-content: center;
		align-items: center;
		width: var(--size-full);
		height: var(--size-full);
	}

	canvas {
		width: var(--size-full);
		height: var(--size-full);
		object-fit: contain;
		overflow: hidden;
	}
</style>
